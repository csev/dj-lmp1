
from django.db import models
from django.utils import timezone

from .context import Context
from .subject import Subject

class ContextLog(models.Model):
    class LOG_TYPE(models.TextChoices):
        NRPS_TOKEN = 'NRPS_TOKEN'
        NRPS_LIST = 'NRPS_LIST'
        NRPS_MEMBER = 'NRPS_MEMBER'
        NRPS_ERROR = 'NRPS_ERROR'
        LineItem_TOKEN = 'LineItem_TOKEN'
        LineItem_CREATE = 'LineItem_CREATE'
        LineItem_ERROR = 'LineItem_ERROR'
        Score_TOKEN = 'Score_TOKEN'
        Score_SEND = 'Score_SEND'
        Score_ERROR = 'Score_ERROR'
        LineItem_UPDATE = 'LineItem_UPDATE'

    id = models.BigAutoField(primary_key=True)
    context = models.ForeignKey(Context, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    type = models.CharField(max_length=20, choices=LOG_TYPE.choices, null=True)
    success = models.BooleanField(default=True)
    http_response = models.IntegerField(null=True)
    status = models.CharField(max_length=200, null=True)
    count = models.BigIntegerField(default=0)
    action = models.TextField(max_length=2000, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    debug_log = models.TextField(null=True)

    def get_positive_hash_code(self):
        return abs(hash(self))

    class Meta:
        db_table = 'PLUS_CONTEXT_LOG'


