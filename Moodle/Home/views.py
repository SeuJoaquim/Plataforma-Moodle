from .forms import NameForm, LoginForm
from .models import User


from django.shortcuts import render, redirect
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
            form_auth= str(User.objects.filter(email=request.POST['email']))
            if form_auth != '<QuerySet []>':    
                p = User.objects.get(email=request.POST['email'])

                if request.POST['senha'] == p.senha:
                    return redirect('/users/'+ p.name,{
                        'form':request.POST})
                else:
                    return render (request, "Home/login.html",{
                    'message': "Senha inválida",
                    'form': form})
            else:
                return render (request, "Home/login.html",{
                    'message': "Email não cadastrado",
                    'form': form})

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

    