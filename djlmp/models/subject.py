import uuid
from django.db import models

from .baselti import BaseLTI
from .tenant import Tenant
from .contextrole import ContextRole

class Subject(BaseLTI):

    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    subject = models.CharField(max_length=BaseLTI.LENGTH_URI, null=False)
    description = models.TextField(max_length=BaseLTI.LENGTH_MEDIUMTEXT, null=True)
    display_name = models.CharField(max_length=BaseLTI.LENGTH_TITLE, null=True, blank=True)
    email = models.CharField(max_length=BaseLTI.LENGTH_TITLE, null=True, blank=True)
    locale = models.CharField(max_length=BaseLTI.LENGTH_TITLE, null=True, blank=True)

    class Meta:
        unique_together = [['tenant', 'subject']]
