
from django.urls import path
from tasks import views
from tasks.views import TransactionAPI
urlpatterns = [
    path('get-transactions/',views.get_transaction),
    path('transactions/',views.TransactionAPI.as_view()),
    path('transactions/modify/', views.TransactionAPI.as_view(), name='transaction-modify'),
    path('transactions/<int:id>/', TransactionAPI.as_view()),

]