from django.conf.urls import url
from django.contrib import admin
from rest_framework.authtoken import views as rest_framework_views

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(
        r'^get_auth_token/$',
        rest_framework_views.obtain_auth_token, name='get_auth_token'),
    url(r'^$', views.index, name='index'),
]
