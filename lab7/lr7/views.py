from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from lr7.forms import RegistrationForm, AuthorizationForm


def main_page(request):
    return render(request, 'index.html')


def error_auth(request):
    return render(request, 'logout.html')


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #login(request, user)
            return HttpResponseRedirect('/success/')
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})


@login_required(login_url='/error/')
def login_success(request):
    # if not request.user.is_authenticated():
        # return HttpResponseRedirect('/')
    return render(request, 'login.html')


def authorization(request):
    if request.method == 'POST':
        form = AuthorizationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data.get('username'), password=data.get('password'))
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/success/')
    else:
        form = AuthorizationForm()
    return render(request, 'authorization.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/error/')
