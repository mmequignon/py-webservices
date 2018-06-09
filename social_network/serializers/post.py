from rest_framework import serializers
from ..models import Post


class PostInputSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(min_value=1)


class PostOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'buddy', 'content', )
