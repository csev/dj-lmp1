from django.db import models

from .baselti import BaseLTI
from .context import Context

class Link(BaseLTI):

    link = models.CharField(max_length=BaseLTI.LENGTH_EXTERNAL_ID, null=False)
    sakai_tool_id = models.CharField(max_length=BaseLTI.LENGTH_SAKAI_ID, null=True)
    context = models.ForeignKey(Context, on_delete=models.CASCADE)
    title = models.CharField(max_length=BaseLTI.LENGTH_TITLE, null=True)
    description = models.TextField(max_length=BaseLTI.LENGTH_MEDIUMTEXT, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['link', 'context_id', 'sakai_tool_id']),
        ]
        unique_together = [
            ['link', 'context'],
        ]

