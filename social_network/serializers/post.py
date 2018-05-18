from rest_framework import serializers
from ..models import Post


class PostInputSerializer(serializers.Serializer):
    id = serializers.IntegerField(min_value=1)


class PostOutputSerializer(serializers.Serializer):
    class Meta:
        model = Post
        fields = ('id', 'buddy', 'parent', 'content', 'comment_ids')
