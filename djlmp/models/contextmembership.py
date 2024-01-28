import uuid
from django.db import models
from django.utils import timezone
from .basedates import BaseDates
from .context import Context
from .subject import Subject

# https://www.imsglobal.org/spec/lti/v1p3/#lis-vocabulary-for-context-roles
# https://docs.djangoproject.com/en/5.0/ref/models/fields/#choices
class ContextRole(models.IntegerChoices):
    LEARNER = 0, "http://purl.imsglobal.org/vocab/lis/v2/membership#Learner"
    INSTRUCTOR = 1, "http://purl.imsglobal.org/vocab/lis/v2/membership#Instructor"
    ADMINISTRATOR = 2, "http://purl.imsglobal.org/vocab/lis/v2/membership#Administrator"
    CONTENTDEVELOPER = 3, "http://purl.imsglobal.org/vocab/lis/v2/membership#ContentDeveloper"
    MENTOR = 4, "http://purl.imsglobal.org/vocab/lis/v2/membership#Mentor"
    MANAGER = 5, "http://purl.imsglobal.org/vocab/lis/v2/membership#Manager"
    MEMBER = 6, "http://purl.imsglobal.org/vocab/lis/v2/membership#Member"
    OFFICER = 7, "http://purl.imsglobal.org/vocab/lis/v2/membership#Officer"

class ContextMembership(BaseDates):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    context = models.ForeignKey(Context, on_delete=models.CASCADE)
    role = models.IntegerField(default=ContextRole.LEARNER, choices=ContextRole.choices)

    # context_role = models.ManyToManyField(ContextRole)


    # def is_instructor(self):
        # return "instructor" in self.lti_roles.lower() or "instructor" in self.lti_roles_override.lower() if self.lti_roles else False

    class Meta:
        unique_together = [
            ['subject', 'context'],
        ]

