from django.urls import path
from djangoApp.views import index

urlpatterns = [
    path('', index, name='index')
]
