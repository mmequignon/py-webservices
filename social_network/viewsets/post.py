from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from ..models import Post
from ..serializers import PostOutputSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer = PostOutputSerializer
