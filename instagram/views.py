
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import authenticate, login as auth_login

# Create your views here.
def signup(request):
    if request.method == 'POST':
        signupform = SignupForm(request.POST)
        if signupform.is_valid():
            user = signupform.save()
            # Log the user in after signup (optional)
            return redirect('login')  # Redirect to the homepage or login page after successful signup
    else:
        signupform = SignupForm()

    return render(request, 'instagram/signup.html', {'signupform': signupform})
# views.py
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm

class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'instagram/login.html'
    success_url = '/home/'  # Adjust the success URL as needed

def home(request):
    return render(request, 'instagram/index.html')