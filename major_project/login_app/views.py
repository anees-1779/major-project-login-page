from django.shortcuts import render, redirect
from django.contrib import messages
from .models import user_auth

# Render the login page
def index(request):
    return render(request, 'login_app/index.html')

# Handle the login submission using the custom model
def submit(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')
        print(user_id)
        # Check if both user_id and password are provided
        if not user_id or not password:
            messages.error(request, "Both User ID and Password are required.")
            return redirect('index')

        try:
            # Query the user_auth model to verify credentials
            user = user_auth.objects.get(user_id=user_id, password=password)
            # If credentials match, redirect to the home page
            return redirect('home')
        except user_auth.DoesNotExist:
            # If no match is found, show an error message
            messages.error(request, "Invalid login details. Please try again.")
            return redirect('index')

    # Redirect to the login page if the request method is not POST
    return redirect('index')

# Render the home page after login
def home(request):
    return render(request, 'login_app/home.html')

def logout(request):
    return render(request,  'login_app/index.html' )