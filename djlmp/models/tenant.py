import uuid
from django.db import models

class Tenant(models.Model):
    LENGTH_GUID = 255
    LENGTH_TITLE = 255
    LENGTH_MEDIUMTEXT = 1000
    LENGTH_EXTERNAL_ID = 255
    LENGTH_SAKAI_ID = 100
    LENGTH_URI = 255

    id = models.BigAutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=LENGTH_TITLE, null=False)
    description = models.TextField(max_length=LENGTH_MEDIUMTEXT, null=True)
    issuer = models.CharField(max_length=LENGTH_EXTERNAL_ID, null=True)
    client_id = models.CharField(max_length=LENGTH_EXTERNAL_ID, null=True)
    deployment_id = models.CharField(max_length=LENGTH_EXTERNAL_ID, null=True)
    trust_email = models.BooleanField(default=True)
    timezone = models.CharField(max_length=100, null=True)
    allowed_tools = models.CharField(max_length=500, null=True)
    new_window_tools = models.CharField(max_length=500, null=True)
    verbose = models.BooleanField(default=False)
    site_template = models.CharField(max_length=LENGTH_SAKAI_ID, null=True)
    realm_template = models.CharField(max_length=LENGTH_SAKAI_ID, null=True)
    inbound_role_map = models.TextField(null=True)
    oidc_auth = models.CharField(max_length=LENGTH_URI, null=True)
    oidc_keyset = models.CharField(max_length=LENGTH_URI, null=True)
    oidc_token = models.CharField(max_length=LENGTH_URI, null=True)
    oidc_audience = models.CharField(max_length=LENGTH_EXTERNAL_ID, null=True)
    retry_at = models.DateTimeField(null=True)
    cache_keyset = models.TextField(null=True)
    oidc_registration_lock = models.CharField(max_length=LENGTH_EXTERNAL_ID, null=True)
    oidc_registration_endpoint = models.CharField(max_length=LENGTH_URI, null=True)
    oidc_registration = models.TextField(null=True)

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

