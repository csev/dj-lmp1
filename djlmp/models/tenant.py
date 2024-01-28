import uuid
from django.db import models

from .baselti import BaseLTI  # assuming BaseLTI is defined in a file named base_lti.py

class Tenant(BaseLTI):

    title = models.CharField(max_length=BaseLTI.LENGTH_TITLE, null=False)
    description = models.TextField(max_length=BaseLTI.LENGTH_MEDIUMTEXT, null=True)
    issuer = models.CharField(max_length=BaseLTI.LENGTH_EXTERNAL_ID, null=True)
    client_id = models.CharField(max_length=BaseLTI.LENGTH_EXTERNAL_ID, null=True, blank=True)
    deployment_id = models.CharField(max_length=BaseLTI.LENGTH_EXTERNAL_ID, null=True, blank=True)
    trust_email = models.BooleanField(default=True)
    timezone = models.CharField(max_length=100, null=True, blank=True)
    oidc_auth = models.CharField(max_length=BaseLTI.LENGTH_URI, null=True, blank=True)
    oidc_keyset = models.CharField(max_length=BaseLTI.LENGTH_URI, null=True, blank=True)
    oidc_token = models.CharField(max_length=BaseLTI.LENGTH_URI, null=True, blank=True)
    oidc_audience = models.CharField(max_length=BaseLTI.LENGTH_EXTERNAL_ID, null=True, blank=True)
    oidc_registration_lock = models.CharField(max_length=BaseLTI.LENGTH_EXTERNAL_ID, null=True, blank=True)
    oidc_registration_endpoint = models.CharField(max_length=BaseLTI.LENGTH_URI, null=True, blank=True)
    oidc_registration = models.TextField(max_length=BaseLTI.LENGTH_MEDIUMTEXT, null=True, blank=True)

    def is_draft(self):
        return (
            not self.issuer
            or not self.client_id
            or not self.oidc_auth
            or not self.oidc_keyset
            or not self.oidc_token
        )

    def validate_deployment_id(self, launch_deployment_id):
        if not self.deployment_id:
            return True
        if self.deployment_id == "*":
            return True
        if self.deployment_id == launch_deployment_id:
            return True
        if launch_deployment_id in self.deployment_id:
            return True
        return False

