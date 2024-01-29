import uuid
from django.db import models

from .basesizes import BaseSizes
from .basedates import BaseDates
from .org import Org

# https://www.imsglobal.org/spec/oneroster/v1p2
class School(BaseDates):

    org = models.ForeignKey(Org, on_delete=models.CASCADE)
    title = models.CharField(max_length=BaseSizes.LENGTH_TITLE, null=False)
    description = models.TextField(max_length=BaseSizes.LENGTH_MEDIUMTEXT, null=True)

