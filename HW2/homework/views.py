import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.files import File
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from homework.forms import RegistrationForm, AuthorizationForm, CommentForm
from homework.models import Good, Comment


@login_required(login_url='/authorization/')
def main(request):
    return HttpResponseRedirect('/goods/')


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            user = authenticate(username=data.get('username'), password=data.get('password'))
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})


def authorization(request):
    if request.method == 'POST':
        form = AuthorizationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data.get('username'), password=data.get('password'))
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = AuthorizationForm()
    return render(request, 'authorization.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/authorization')


class GoodsView(View):
    def get(self, request):
        goods = Good.objects.all()[:10]
        return render(request, 'goods.html', {'goods': goods, 'user': request.user.get_full_name})


class GoodView(View):
    def get(self, request, id):
        good = Good.objects.filter(id__exact=id)[0]
        users = good.user_comment.all()
        form = CommentForm()
        dictionary = {
            'good': good,
            'user': request.user.get_full_name(),
            'users': users,
            'form': form,
        }
        return render(request, 'good.html', dictionary)


def add_good(request):
    if request.method == 'POST':
        good = Good()
        good.logo = request.FILES.get('logo')
        good.name = request.POST.get('name')
        good.price = request.POST.get('price')
        good.description = request.POST.get('description')
        good.save()
        return HttpResponseRedirect('/goods')
    return HttpResponseRedirect('/')


class WriteComment(View):
    def post(self, request, id):
        if request.is_ajax():
            form = CommentForm(request.POST)
            good = Good.objects.filter(id__exact=id)[0]
            if form.is_valid():
                data = form.cleaned_data
                comment = Comment()
                comment.user = request.user
                comment.good = good
                comment.text = data.get('text')
                comment.save()
            user = request.user.username
            return HttpResponse(json.dumps({'message': user}))


class AddContent(View):
    def post(self, request):
        if request.is_ajax():
            last_good_id = int(request.POST.get('last_good_id'))
            goods = Good.objects.all()
            if last_good_id == goods.count():
                return HttpResponse(json.dumps({'message': 'stop'}))
            good = goods[last_good_id:last_good_id + 1][0]
            data = {
                'good_id': good.id,
                'good_logo': good.logo.url,
                'good_name': good.name,
                'good_description': good.description
            }
            return HttpResponse(json.dumps({'message': data}))
