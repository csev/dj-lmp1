import uuid
from django.db import models

from .baselti import BaseLTI
from .tenant import Tenant

class Context(BaseLTI):

    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    title = models.CharField(max_length=BaseLTI.LENGTH_TITLE, null=True)
    description = models.TextField(max_length=BaseLTI.LENGTH_MEDIUMTEXT, null=True)
    deployment_id = models.CharField(max_length=BaseLTI.LENGTH_EXTERNAL_ID, null=True)
    label = models.CharField(max_length=BaseLTI.LENGTH_TITLE, null=True, blank=True)
    line_items = models.CharField(max_length=BaseLTI.LENGTH_URI, null=True, blank=True)
    line_items_token = models.CharField(max_length=BaseLTI.LENGTH_URI, null=True, blank=True)
    grade_token = models.CharField(max_length=BaseLTI.LENGTH_URI, null=True, blank=True)
    context_memberships = models.CharField(max_length=BaseLTI.LENGTH_URI, null=True, blank=True)
    nrps_token = models.CharField(max_length=BaseLTI.LENGTH_URI, null=True, blank=True)
    nrps_start = models.DateTimeField(null=True, blank=True)
    nrps_finish = models.DateTimeField(null=True, blank=True)
    nrps_status = models.CharField(max_length=BaseLTI.LENGTH_TITLE, null=True, blank=True)
    nrps_count = models.BigIntegerField(null=True, blank=True)

