import uuid
from django.db import models

from .basesizes import BaseSizes  
from .baselaunchable import BaseLaunchAble  
from .tenant import Tenant

class Context(BaseLaunchAble):

    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    title = models.CharField(max_length=BaseSizes.LENGTH_TITLE, null=True)
    description = models.TextField(max_length=BaseSizes.LENGTH_MEDIUMTEXT, null=True, blank=True)
    # On Canvas deployment_id changes a lot - per course sometimes - is that correct?
    deployment_id = models.CharField(max_length=BaseSizes.LENGTH_EXTERNAL_ID, null=True, blank=True)
    label = models.CharField(max_length=BaseSizes.LENGTH_TITLE, null=True, blank=True)
    line_items = models.CharField(max_length=BaseSizes.LENGTH_URI, null=True, blank=True)
    line_items_token = models.CharField(max_length=BaseSizes.LENGTH_URI, null=True, blank=True)
    grade_token = models.CharField(max_length=BaseSizes.LENGTH_URI, null=True, blank=True)
    context_memberships = models.CharField(max_length=BaseSizes.LENGTH_URI, null=True, blank=True)
    nrps_token = models.CharField(max_length=BaseSizes.LENGTH_URI, null=True, blank=True)
    nrps_start = models.DateTimeField(null=True, blank=True)
    nrps_finish = models.DateTimeField(null=True, blank=True)
    nrps_status = models.CharField(max_length=BaseSizes.LENGTH_TITLE, null=True, blank=True)
    nrps_count = models.BigIntegerField(null=True, blank=True)

