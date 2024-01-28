import uuid
from django.db import models
from django.utils import timezone
from .baselti import BaseLTI
from .context import Context
from .subject import Subject
from .contextrole import ContextRole

class ContextMembership(BaseLTI):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    context = models.ForeignKey(Context, on_delete=models.CASCADE)

# https://www.imsglobal.org/spec/lti/v1p3/#lis-vocabulary-for-context-roles

# https://docs.djangoproject.com/en/5.0/ref/models/fields/#choices

    ADMINISTRATOR = "http://purl.imsglobal.org/vocab/lis/v2/membership#Administrator"
    INSTRUCTOR = "http://purl.imsglobal.org/vocab/lis/v2/membership#Instructor"
    CONTENTDEVELOPER = "http://purl.imsglobal.org/vocab/lis/v2/membership#ContentDeveloper"
    LEARNER = "http://purl.imsglobal.org/vocab/lis/v2/membership#Learner"
    MENTOR = "http://purl.imsglobal.org/vocab/lis/v2/membership#Mentor"
    MANAGER = "http://purl.imsglobal.org/vocab/lis/v2/membership#Manager"
    MEMBER = "http://purl.imsglobal.org/vocab/lis/v2/membership#Member"
    OFFICER = "http://purl.imsglobal.org/vocab/lis/v2/membership#Officer"

    CONTEXT_ROLE_CHOICES = {
        ADMINISTRATOR: "Administrator",
        INSTRUCTOR: "Instructor",
        CONTENTDEVELOPER: "Content Developer",
        LEARNER: "Learner",
        MENTOR: "Mentor",
        MANAGER: "Manager",
        MEMBER: "Member",
        OFFICER: "Officer",
    }

    context_role = models.ManyToManyField(ContextRole)

    def is_instructor(self):
        return "instructor" in self.lti_roles.lower() or "instructor" in self.lti_roles_override.lower() if self.lti_roles else False

    class Meta:
        unique_together = [
            ['subject', 'context'],
        ]

