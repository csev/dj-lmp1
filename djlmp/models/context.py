import uuid
from django.db import models

from .baselti import BaseLTI
from .tenant import Tenant

class Context(BaseLTI):
    BaseLTI.LENGTH_GUID = 255
    BaseLTI.LENGTH_EXTERNAL_ID = 255
    BaseLTI.LENGTH_SAKAI_ID = 100
    BaseLTI.LENGTH_TITLE = 255
    BaseLTI.LENGTH_URI = 255

    context = models.CharField(max_length=BaseLTI.LENGTH_EXTERNAL_ID, null=False)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    deployment_id = models.CharField(max_length=BaseLTI.LENGTH_EXTERNAL_ID, null=True)
    sakai_site_id = models.CharField(max_length=BaseLTI.LENGTH_SAKAI_ID, null=True)
    title = models.CharField(max_length=BaseLTI.LENGTH_TITLE, null=True)
    label = models.CharField(max_length=BaseLTI.LENGTH_TITLE, null=True)
    line_items = models.CharField(max_length=BaseLTI.LENGTH_URI, null=True)
    line_items_token = models.CharField(max_length=BaseLTI.LENGTH_URI, null=True)
    grade_token = models.CharField(max_length=BaseLTI.LENGTH_URI, null=True)
    context_memberships = models.CharField(max_length=BaseLTI.LENGTH_URI, null=True)
    nrps_token = models.CharField(max_length=BaseLTI.LENGTH_URI, null=True)
    nrps_start = models.DateTimeField(null=True)
    nrps_finish = models.DateTimeField(null=True)
    nrps_status = models.CharField(max_length=BaseLTI.LENGTH_TITLE, null=True)
    nrps_count = models.BigIntegerField(null=True)

