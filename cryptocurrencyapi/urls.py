from django.urls import path
from .views import list

app_name = 'cryptocurrencyapi'

urlpatterns = [
    path('api/', list, name='api'),
]