from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from ..models import Buddy
from ..serializers import BuddyOutputSerializer


class BuddyViewSet(viewsets.ModelViewSet):
    queryset = Buddy.objects.all()
    serializer_class = BuddyOutputSerializer
