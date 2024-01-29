import uuid
from django.utils import timezone
from django.db import models

class BaseDates(models.Model):
    created_at = models.DateTimeField(null=True)
    modifier = models.CharField(max_length=42, null=True)
    modified_at = models.DateTimeField(null=True)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True)
    deletor = models.CharField(max_length=42, null=True)

    # https://stackoverflow.com/a/77892185/1994792
    def get_excluded_field_names():
        return [f.name for f in BaseDates._meta.fields]

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        super().save(*args, **kwargs)

    class Meta:
        abstract = True

