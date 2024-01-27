import uuid
from django.db import models

from .baselti import BaseLTI
from .tenant import Tenant

class Subject(BaseLTI):

    sakai_user_id = models.CharField(max_length=BaseLTI.LENGTH_SAKAI_ID, null=True)
    subject = models.CharField(max_length=BaseLTI.LENGTH_URI, null=False)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=BaseLTI.LENGTH_TITLE, null=True)
    email = models.CharField(max_length=BaseLTI.LENGTH_TITLE, null=True)
    locale = models.CharField(max_length=BaseLTI.LENGTH_TITLE, null=True)
