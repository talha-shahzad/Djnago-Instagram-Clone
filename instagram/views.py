from django.shortcuts import render
from django.contrib.auth import authenticate, login
# Create your views here.



def index(request):
    return render(request, 'instagram/index.html', {'user': request.user})
