
from django.conf.urls import url
from django.contrib import admin
from lr7.views import registration, main_page, login_success, authorization, logout_view, error_auth

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main_page, name='main'),
    url(r'^registration/', registration, name='registration'),
    url(r'^authorization/', authorization, name='authorization'),
    url(r'^success/', login_success),
    url(r'^error/', error_auth, name='error_auth'),
    url(r'^logout/', logout_view, name='logout'),
]
