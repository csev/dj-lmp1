import uuid
from django.db import models

from .basesizes import BaseSizes
from .baselaunchable import BaseLaunchAble
from .tenant import Tenant

class Subject(BaseLaunchAble):

    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    subject = models.CharField(max_length=BaseSizes.LENGTH_URI, null=False)
    description = models.TextField(max_length=BaseSizes.LENGTH_MEDIUMTEXT, null=True, blank=True)
    display_name = models.CharField(max_length=BaseSizes.LENGTH_TITLE, null=True, blank=True)
    email = models.CharField(max_length=BaseSizes.LENGTH_TITLE, null=True, blank=True)
    locale = models.CharField(max_length=BaseSizes.LENGTH_TITLE, null=True, blank=True)

    class Meta:
        unique_together = [['tenant', 'subject']]
