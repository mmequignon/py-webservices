from rest_framework import serializers
from django.contrib.auth import get_user_model


class BuddyInputSerializer(serializers.Serializer):
    id = serializers.IntegerField(min_value=1)


class BuddyOutputSerializer(serializers.Serializer):
    buddy_ids = serializers.StringRelatedField(many=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'buddy_ids')  # 'attributes.buddy_ids')
