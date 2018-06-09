from rest_framework import serializers
from ..models import Comment


class CommentInputSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(min_value=1)


class CommentOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'buddy', 'parent', 'content', )
