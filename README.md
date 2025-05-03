Setup Instructions and steps:

step1. Create the Django Project & App
    django-admin startproject todo
    cd todo
    python manage.py startapp tasks
    
step2. Add apps to settings.py
INSTALLED_APPS = [
  "rest_framework",
  "tasks"
]

step3. Create the Model

step4. Run Migrations
      py manage.py makemigrations
      py manage.py migrate
      
step4. Create admin

step5. create super user
   py manage.py createsuperuser
   
step6. Create the Serializer in application level

step7. Create the Views

step8. Create a folder name api and inside this Create urls.py in application level

step9. Include this application urls.py into project level urls.py

step10. Run the server
   py manage.py runserver
