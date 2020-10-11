from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from Account.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm
# Create your views here.



def register(request):
    
    context = {}
    if request. POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['register_form'] = form
    else: 
        form = RegistrationForm()
        context['register_form'] = form
    return render(request, 'Account/register.html', context)


def logout_view(request):
    logout(request)
    return redirect("home")


def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('home')
    

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            
            if user:
                login(request, user)
                return redirect('home')

        
    else:
        form = AccountAuthenticationForm(request.POST)
        form.errors.clear()

    
    context['login_form'] = form
    return render(request, 'Account/login.html', context)

def account(request):
    
    if not request.user.is_authenticated:
        return redirect("login")
    context = {}
    context['email'] = request.user.email
    context['username'] = request.user.username
    context['is_professor'] = request.user.is_professor
    context['last_login'] = request.user.last_login
    
    return render(request, "Account/account.html", context)
    

def account_view(request):

    if not request.user.is_authenticated:
        return redirect("login")

    context = {}
    context['is_professor'] = request.user.is_professor
    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.initial ={
                "email": request.POST['email'],
                "username": request.POST['username'],
            }
            form.save()
            context['sucess_message'] = 'Updated'
    else:
        form = AccountUpdateForm(
            initial = {
                "email": request.user.email,
                "username": request.user.username,
            }
        )
    context['account_form'] = form
    return render(request, "Account/user.html", context)

def professor_auth(request):
    user = request.user
    if user.is_authenticated:
        user.is_professor = True
        user.save()
    return redirect("account")
    