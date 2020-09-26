from .forms import NameForm, LoginForm
from .models import User


from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.

message = " "
def index(request):
    return render (request, "Home/index.html")

def login(request):
    if request.method =='POST':
        form= LoginForm(request.POST)
        if form.is_valid():
            User.objects.filter(email=request.POST['email'])
            return render (request, "Home/user.html",{
                'form':request.POST
            })

    else:
        form = LoginForm()

    return render (request, "Home/login.html",{
        'form':form
    })


def register(request):
    
    if request.method =='POST':
        form= NameForm(request.POST)
        if form.is_valid():
            user_auth= User.objects.filter(email=request.POST['email'])
            t = str(user_auth)
            if (t =='<QuerySet []>'):            
                forms= request.POST
                user = User()
                user.name = forms['name'] 
                user.email = forms['email']
                user.senha = forms['senha'] 
                user.tipo = forms['tipo']
                user.save()
                return render (request, "Home/user.html",{
                'form':request.POST})
            else:
                return render (request, "Home/register.html",{
                'message': "Invalid credentials",
                'form': form})
                                  
    else:
        form = NameForm()

    return render (request, "Home/register.html",{
        'form':form
    })

    