import uuid
from django.db import models

from .basesizes import BaseSizes
from .basedates import BaseDates
from .link import Link
from .context import Context

class LineItem(BaseDates):
    context = models.ForeignKey('Context', on_delete=models.CASCADE)
    link = models.OneToOneField('Link', on_delete=models.CASCADE, null=True)
    resource_id = models.CharField(max_length=BaseSizes.LENGTH_EXTERNAL_ID, null=True)
    tag = models.CharField(max_length=BaseSizes.LENGTH_EXTERNAL_ID, null=True)
    label = models.CharField(max_length=BaseSizes.LENGTH_TITLE, null=True)
    score_maximum = models.FloatField(null=True)
    start_date_time = models.DateTimeField(null=True)
    end_date_time = models.DateTimeField(null=True)
