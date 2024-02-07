from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import RegistrationForm

def index(request):
    return render(request, 'mainpages/index.html')

def about(request):
    return render(request, 'mainpages/about.html')

def contact(request):
    return render(request, 'mainpages/contact.html')

def cookies(request):
    return render(request, 'mainpages/cookies.html')

def privacypolicy(request):
    return render(request, 'mainpages/privacypolicy.html')

def registerPage(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully created')
            return redirect('login')

    context = {'form': form}
    return render(request, 'mainpages/register.html', context)


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('articles_home')
        else:
            messages.info(request, 'You have entered wrong username or password.')

    return render(request, 'mainpages/login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')