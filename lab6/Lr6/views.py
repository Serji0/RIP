from django.shortcuts import render
from django.views import View

from Lr6.models import Good, User


def main_page(request):
    return render(request, 'index.html')


class good_view(View):
    def get(self, request):
        goods = Good.objects.all()
        return render(request, 'goods.html', {'goods': goods})


class user_view(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'users.html', {'users': users})