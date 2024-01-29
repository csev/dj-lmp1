import uuid
from django.db import models

from .basedates import BaseDates
from .basesizes import BaseSizes

# https://www.imsglobal.org/spec/oneroster/v1p2
class KeySet(BaseDates):

    title = models.CharField(max_length=BaseSizes.LENGTH_TITLE, null=False)
    description = models.TextField(max_length=BaseSizes.LENGTH_MEDIUMTEXT, null=True)
    public = models.TextField(max_length=BaseSizes.LENGTH_MEDIUMTEXT, null=True)
    private = models.TextField(max_length=BaseSizes.LENGTH_MEDIUMTEXT, null=True)

