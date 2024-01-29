import uuid
from django.db import models

from .basesizes import BaseSizes
from .basedates import BaseDates

# https://www.imsglobal.org/spec/oneroster/v1p2
class Org(BaseDates):

    title = models.CharField(max_length=BaseSizes.LENGTH_TITLE, null=False)
    description = models.TextField(max_length=BaseSizes.LENGTH_MEDIUMTEXT, null=True)

