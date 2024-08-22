
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from .models import User

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


def profile(request):

    return render(request, 'instagram/profile.html', {'user': request.user})



def home(request):
    suggestions = User.objects.exclude(id=request.user.id).exclude(is_superuser=True)[:10]
    

    print(suggestions)
    
    return render(request, 'instagram/index.html', {'user': request.user, 'suggestions': suggestions})


@login_required
def editProfile(request):
    user = request.user
    print(user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page or any other page
    else:
        form = UserProfileForm(instance=user)

    return render(request, 'instagram/editProfile.html', {'form': form})
