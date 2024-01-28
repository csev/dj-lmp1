from django.db import models

from .basesizes import BaseSizes
from .baselaunchable import BaseLaunchAble
from .context import Context

class Link(BaseLaunchAble):

    link = models.CharField(max_length=BaseSizes.LENGTH_EXTERNAL_ID, null=False)
    context = models.ForeignKey(Context, on_delete=models.CASCADE)
    title = models.CharField(max_length=BaseSizes.LENGTH_TITLE, null=True)
    description = models.TextField(max_length=BaseSizes.LENGTH_MEDIUMTEXT, null=True, blank=True)

    class Meta:
        unique_together = [
            ['link', 'context'],
        ]

