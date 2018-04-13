from django.db import models
from .content import Content


class Comment(Content):
    parent = models.ForeignKey(
        'Content',
        on_delete=models.CASCADE,
        related_name="comment_ids")
