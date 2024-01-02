# Sjango 
from django.urls import path
# Apps : User
from apps.users.api.api import  user_api_view, user_detail_api_view


urlpatterns = [
    path('user/', user_api_view, name='users_api'),
    path('user/<int:pk>', user_detail_api_view, name='users_detail'),
]

