from django.urls import path
from .views import register, staff_login
from django.contrib.auth import views as auth_views


app_name = 'users'


urlpatterns = [
    path('register/', register, name='register'),
    path('', staff_login, name='login'),
    #path('logout/', logout, name='logout'),
]
