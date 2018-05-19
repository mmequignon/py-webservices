from django.conf.urls import url, include
from django.contrib import admin

from rest_framework.authtoken import views as rest_framework_views
from rest_framework.routers import DefaultRouter

from .viewsets import BuddyViewSet, CommentViewSet, PostViewSet

router = DefaultRouter()
router.register(r'buddy', BuddyViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'post', PostViewSet)


urlpatterns = [
    #  url(r'^admin/', admin.site.urls),
    url(
        r'^get_auth_token/$',
        rest_framework_views.obtain_auth_token, name='get_auth_token'),
    url(r'^', include(router.urls)),
]
