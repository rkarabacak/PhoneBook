import accounts
from accounts.forms import LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout



def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('book:index')
    return render(request, 'accounts/form.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('accounts:login')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('book:index')
    else:
        form = UserCreationForm()
        context = {
            'form': form
        }
    return render(request, 'accounts/signup.html', context)