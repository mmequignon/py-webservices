from rest_framework import serializers
from django.contrib.auth import get_user_model


class BuddyInputSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(min_value=1)


class BuddyOutputSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', )
