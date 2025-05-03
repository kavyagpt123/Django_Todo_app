from django.core.serializers import serialize
from django.shortcuts import render
from .models import Transactions
from rest_framework.response import Response
from .serializers import TransactionsSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
# Create your views here.

@api_view(["GET","POST"])
# List of all the tasks
def get_transaction(request):
    if request.method == 'GET':
        queryset = Transactions.objects.all()

        #Search by title '?search=title'
        search_title = request.query_params.get('search')
        if search_title:
            queryset = queryset.filter(title__icontains=search_title)

        #Search by date '?search_date=2025-05-01'
        search_date = request.query_params.get('search_date')
        if search_date:
            queryset = queryset.filter(date=search_date)

        #Sort by date if 'sort_by_date=true'
        sort_by_date = request.query_params.get('sort_by_date')
        # ascending
        if sort_by_date == 'true':
            queryset = queryset.order_by('date')
            # descending
        elif sort_by_date == 'desc':
            queryset = queryset.order_by('-date')
            # default fallback
        else:
            queryset = queryset.order_by('-pk')

        serializer = TransactionsSerializer(queryset, many=True)
        return Response({"data": serializer.data})

    if request.method == 'POST':
        serializer = TransactionsSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                "message": "data not saved",
                "errors": serializer.errors,
            })
        serializer.save()
        return Response({
            "message": "data saved",
            "data": serializer.data
        })

    queryset=Transactions.objects.all().order_by('-pk')
    serializer=TransactionsSerializer(queryset, many=True)

    return Response(
        {
            "data": serializer.data
        }
    )

class TransactionAPI(APIView):
    # get all tasks
    def get(self,request):
        return Response({
            "message": "this is get method"
        })
    #Add a task
    def post(self,request):
        data=request.data
        serializer=TransactionsSerializer(data=data)
        if not serializer.is_valid():
            return Response({
                "message": "data not saved",
                "errors": serializer.errors,
            })
        serializer.save()
        return Response({
            "message": "data saved",
            "data": serializer.data
        })

    # def put(self,request):
    #     return Response({
    #         "message": "this is put method"
    #     })
    #Edits a task
    def patch(self,request):
        data= request.data

        if not data.get('id'):
            return Response({
                "message": "data not updated",
                "errors": "id is required",
            })
        transaction=Transactions.objects.get(id=data.get('id'))
        serializer=TransactionsSerializer(transaction, data=data, partial=True)
        if not serializer.is_valid():
            return Response({
                "message": "data not saved",
                "errors": serializer.errors,
            })
        serializer.save()
        return Response({
            "message": "data saved",
            "data": serializer.data
        })
    #Delete a task(Delete/tasks/{id}
    def delete(self,request):
        data= request.data

        if not data.get('id'):
            return Response({
                "message": "data not updated",
                "errors": "id is required",
            })
        transaction = Transactions.objects.get(id=data.get('id')).delete()

        return Response({
            "message": "data deleted",
            "data": {}
        })
