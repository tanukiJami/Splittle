from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm

def landingPage(request):
    return render(request, 'landingPage.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print("Authenticated user:", user)
        if user is not None:
            auth_login(request, user)
            return redirect('homePage')  # Redirect to 'home' after successful login
        else:
            # If authentication fails, return the login page with an error
            return render(request, 'landingPage.html', {'error': 'Invalid login credentials'})
    
    # If it's a GET request (e.g., when visiting the login page), render the page
    return render(request, 'landingPage.html')
    
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            return redirect('homePage')
    else:
        form = CustomUserCreationForm()
    #If form is invalid, reloads register with the form
    return render(request, 'register.html', {'form': form})
