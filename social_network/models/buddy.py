from django.contrib.auth.models import User


class Buddy(User):

    class Meta:
        proxy = True
