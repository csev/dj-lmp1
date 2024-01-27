from django.db import models
from django.utils import timezone
from .baselti import BaseLTI
from .context import Context
from .subject import Subject

class Membership(BaseLTI):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    context = models.ForeignKey(Context, on_delete=models.CASCADE)
    lti_roles = models.TextField(null=True)
    lti_roles_override = models.TextField(null=True)

    def is_instructor(self):
        return "instructor" in self.lti_roles.lower() or "instructor" in self.lti_roles_override.lower() if self.lti_roles else False

    class Meta:
        indexes = [
            models.Index(fields=['subject_id', 'context_id']),
        ]
        unique_together = [
            ['subject', 'context'],
        ]


