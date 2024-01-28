from django.apps import AppConfig


class DjlmpConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'djlmp'

    # This causes a warning: avoid executing queries in AppConfig.ready()
    # Later we will find a better way to fix this
    def ready(self) :
        from .models import ContextRole
        for role in ContextRole.CONTEXT_ROLE_CHOICES:
            c, created = ContextRole.objects.get_or_create(context_role=role)
            if created : print(role)
