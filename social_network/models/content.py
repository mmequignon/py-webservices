from django.db import models


class Content(models.Model):
    buddy = models.ForeignKey(
        'Buddy',
        on_delete=models.CASCADE,
        verbose_name="Creator")
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    write_date = models.DateTimeField(auto_now=True)
