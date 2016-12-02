from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

data = {'goods': []}
for i in range(1, 5):
    data['goods'].append(
        {
            'id': i,
            'title': '{0}{1}'.format('Товар №', i),
            'description': 'Товар № '+ str(i),
            'text': 'Товар № '+ str(i),
            'date': '02.12.2016'
        }
    )


def main_page(request):
    return render(request, 'goods.html', data)


class goods_view(View):
    def get(self, request, id):
        data_good = {
            'good': data['goods'][int(id) - 1]
        }
        return render(request, 'good.html', data_good)

