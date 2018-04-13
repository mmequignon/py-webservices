from django.db import models


class Feeling(models.Model):
    feeling_type = models.TextField(
        max_length=2,
        choices=(('PO', 'poo'), ('BR', 'beer')),
        help_text="""This field determines the kind of feeling of a buddy """
                  """about a content.""")
    content = models.ForeignKey(
        'Content',
        on_delete=models.CASCADE,
        related_name="feeling_ids",)
    buddy = models.ForeignKey(
        'Buddy',
        on_delete=models.CASCADE,
        related_name="feeling_ids")
