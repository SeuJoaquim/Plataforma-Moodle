from .forms import NameForm


from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    return render (request, "Home/index.html")

def login(request):
    if request.method =='POST':
        form= NameForm(request.POST)
        if form.is_valid():
            return render (request, "Home/user.html",{
                'form':request.POST
            })

    else:
        form = NameForm()

    return render (request, "Home/login.html",{
        'form':form
    })

def register(request):
    if request.method =='POST':
        form= NameForm(request.POST)
        if form.is_valid():
            return render (request, "Home/user.html",{
                'form':request.POST
            })

    else:
        form = NameForm()

    return render (request, "Home/login.html",{
        'form':form
    })

    