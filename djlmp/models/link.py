from django.db import models

from .baselti import BaseLTI
from .context import Context

class Link(BaseLTI):
    LENGTH_GUID = 36
    LENGTH_EXTERNAL_ID = 255
    LENGTH_TITLE = 255
    LENGTH_SAKAI_ID = 100
    LENGTH_MEDIUMTEXT = 4000  # Less than 4096 because Oracle

    link = models.CharField(max_length=LENGTH_EXTERNAL_ID, null=False)
    sakai_tool_id = models.CharField(max_length=LENGTH_SAKAI_ID, null=True)
    context = models.ForeignKey(Context, on_delete=models.CASCADE)
    title = models.CharField(max_length=LENGTH_TITLE, null=True)
    description = models.TextField(max_length=LENGTH_MEDIUMTEXT, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['link', 'context_id', 'sakai_tool_id']),
        ]
        unique_together = [
            ['link', 'context'],
        ]

