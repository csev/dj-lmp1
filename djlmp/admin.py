from django.contrib import admin

from .models import Tenant, Context, Subject, Link, LineItem, Membership, Score, ContextLog

admin.site.register(Tenant)
admin.site.register(Context)
admin.site.register(Subject)
admin.site.register(Link)
admin.site.register(LineItem)
admin.site.register(Membership)
admin.site.register(Score)
admin.site.register(ContextLog)

# Register your models here.
