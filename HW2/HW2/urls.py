
from django.conf.urls import url
from django.contrib import admin
from homework.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main, name='main'),
    url(r'^registration/', registration, name='registration'),
    url(r'^authorization/', authorization, name='authorization'),
    url(r'^logout/', logout_view, name='logout'),
    url(r'^goods/', GoodsView.as_view(), name='goods'),
    url(r'^good/(?P<id>\d+)', GoodView.as_view(), name='good'),
    url(r'^add_good/', add_good, name='add_good'),
    url(r'^write_comment/(?P<id>\d+)', WriteComment.as_view(), name='write_comment'),
    url(r'^add_content', AddContent.as_view(), name='add_content'),
]


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
