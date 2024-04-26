# auth_app/urls.py
from django.urls import path
from .views import signup, custom_login, custom_logout

app_name = 'auth_app'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),
]
