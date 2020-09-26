from django.shortcuts import render
from Home.models import User

# Create your views here.

def user(request, user_name):
    user= User.objects.get(name=user_name)
    return render(request,"Interface/user.html", {
        'form': user
    })