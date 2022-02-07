from django.urls import path
from .views import template

app_name = 'imports'

urlpatterns = [
    path('import-and-read/', template, name='import-and-read'),
]
