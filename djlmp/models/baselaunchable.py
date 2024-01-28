import uuid
from django.utils import timezone
from django.db import models

class BaseLaunchAble(models.Model):
    LENGTH_GUID = 36
    LENGTH_URI = 500
    LENGTH_TITLE = 500
    LENGTH_EXTERNAL_ID = 200
    LENGTH_MEDIUMTEXT = 4000  # Less than 4096 because Oracle
    LENGTH_SAKAI_ID = 99

    class Meta:
        abstract = True

    id = models.BigAutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    login_count = models.IntegerField(null=True)
    login_ip = models.CharField(max_length=64, null=True)
    login_subject = models.CharField(max_length=42, null=True)
    login_at = models.DateTimeField(null=True)
    json = models.TextField(null=True)


    # https://stackoverflow.com/a/77892185/1994792
    def get_exclude_field_names():
        return [f.name for f in BaseLaunchAble._meta.fields]

    # basedates.py
    created_at = models.DateTimeField(null=True)
    modifier = models.CharField(max_length=LENGTH_SAKAI_ID, null=True)
    modified_at = models.DateTimeField(null=True)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True)
    deletor = models.CharField(max_length=LENGTH_SAKAI_ID, null=True)

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        super().save(*args, **kwargs)
