from django.urls import path
from djangoApp.views import index, tasks, create_task

urlpatterns = [
    path('', index, name='index'),
    path('tasks/', tasks, name='tasks'),
    path('create/', create_task, name='create'),
    path('editar/id', editar, name='editar'),



]
