import uuid
from django.db import models

# https://www.imsglobal.org/spec/lti/v1p3/#lis-vocabulary-for-context-roles

# https://docs.djangoproject.com/en/5.0/ref/models/fields/#choices

class ContextRole(models.Model):

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

    context_role = models.CharField(
        max_length=100,
        choices=CONTEXT_ROLE_CHOICES,
        default=LEARNER,
        unique=True,
    )

    def __str__(self):
        return self.CONTEXT_ROLE_CHOICES[self.context_role];

