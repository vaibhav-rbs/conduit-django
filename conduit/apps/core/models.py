from django.db import models

class TimestampModel(models.Model):

    created_at = models.DateTimeField(auto_now=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

        ordering = ['-created_at', '-updated_at']
