from django.db import models


class BuddyExtension(models.Model):
    buddy = models.OneToOneField(
        'Buddy',
        on_delete=models.CASCADE,
        related_name="attributes")
    buddy_ids = models.ManyToManyField(
        'Buddy',
        blank=True)

    def __str__(self):
        return self.buddy_id.__str__()
