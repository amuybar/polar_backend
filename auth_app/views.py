# auth_app/views.py
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse

def signup(request):
    # Handle signup logic
    return JsonResponse({"message": "User signed up successfully"})

def custom_login(request):
    # Handle login logic
    return JsonResponse({"message": "User logged in successfully"})

def custom_logout(request):
    # Handle logout logic
    return JsonResponse({"message": "User logged out successfully"})
