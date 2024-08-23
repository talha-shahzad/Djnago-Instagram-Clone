
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from .models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

@login_required
def logout_view(request):
    # Log the user out
    print(request.user)
    logout(request)
    print(request.user)
    # Redirect to the login page after logout
    return redirect('login')  # Replace 'login' with the name of your login URL pattern


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


from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm

class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'instagram/login.html'
    success_url = '/home/'  # Adjust the success URL as needed




def profile(request, username):
    user = get_object_or_404(User, username=username)
    follower_count = user.followers.count()
    following_count = user.following.count()  # Assuming you want to show following count as well

    context = {
        'user': user,
        'follower_count': follower_count,
        'following_count': following_count,
    }
    return render(request, 'instagram/profile.html', context)


@login_required(login_url='login')
def home(request):
    suggestions = User.objects.exclude(id=request.user.id).exclude(is_superuser=True)[:10]
    return render(request, 'instagram/index.html', {'user': request.user, 'suggestions': suggestions})

def search(request):
    if request.method == 'GET':
        query = request.GET.get('search')
        if query:
            results = User.objects.filter(
                                            Q(username__icontains=query) | Q(first_name__icontains=query) | Q(last_name__icontains=query)
                                            ).exclude(
                                            id=request.user.id
                                            ).exclude(
                                            is_superuser=True
                                        )

            return render(request, 'instagram/search.html', {'results': results})
    return render(request, 'instagram/search.html')

@login_required(login_url='login')
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


@login_required
def toggle_follow(request, username):
    target_user = get_object_or_404(User, username=username)
    if request.user.username == username:
        return JsonResponse({'error': 'Cannot follow yourself'}, status=400)

    if request.user in target_user.followers.all():
        target_user.followers.remove(request.user)
        action = 'unfollowed'
    else:
        target_user.followers.add(request.user)
        action = 'followed'

    return JsonResponse({'action': action})
