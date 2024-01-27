from django.db import models
import uuid

class BaseLTI(models.Model):
    LENGTH_GUID = 36
    LENGTH_URI = 500
    LENGTH_TITLE = 500
    LENGTH_EXTERNAL_ID = 200
    LENGTH_MEDIUMTEXT = 4000  # Less than 4096 because Oracle
    LENGTH_SAKAI_ID = 99

    id = models.BigAutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    updated_at = models.DateTimeField(null=True)
    sent_at = models.DateTimeField(null=True)
    success = models.BooleanField(default=True)
    status = models.CharField(max_length=200, null=True)
    debug_log = models.TextField(null=True)
    created_at = models.DateTimeField(null=True)
    modifier = models.CharField(max_length=LENGTH_SAKAI_ID, null=True)
    modified_at = models.DateTimeField(null=True)
    deleted = models.BooleanField(default=False)
    deletor = models.CharField(max_length=LENGTH_SAKAI_ID, null=True)
    deleted_at = models.DateTimeField(null=True)
    login_count = models.IntegerField(null=True)
    login_ip = models.CharField(max_length=64, null=True)
    login_user = models.CharField(max_length=LENGTH_SAKAI_ID, null=True)
    login_at = models.DateTimeField(null=True)
    json = models.TextField(null=True)

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        super().save(*args, **kwargs)

    class Meta:
        abstract = True

