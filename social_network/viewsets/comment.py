from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from ..models import Comment
from ..serializers import CommentOutputSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentOutputSerializer
