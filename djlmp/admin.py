from django.contrib import admin

from .models import Tenant
from .models import Subject
from .models import Context, ContextMembership
from .models import Link, LineItem, Score

from .models import BaseLaunchAble

# https://stackoverflow.com/a/77892185/1994792
class TenantAdmin(admin.ModelAdmin):
    exclude = BaseLaunchAble.get_exclude_field_names();
admin.site.register(Tenant, TenantAdmin)

class ContextAdmin(admin.ModelAdmin):
    exclude = BaseLaunchAble.get_exclude_field_names();
admin.site.register(Context, ContextAdmin)

class SubjectAdmin(admin.ModelAdmin):
    exclude = BaseLaunchAble.get_exclude_field_names();
admin.site.register(Subject, SubjectAdmin)

class LinkAdmin(admin.ModelAdmin):
    exclude = BaseLaunchAble.get_exclude_field_names();
admin.site.register(Link, LinkAdmin)

class LineItemAdmin(admin.ModelAdmin):
    exclude = BaseLaunchAble.get_exclude_field_names();
admin.site.register(LineItem, LineItemAdmin)

class ContextMembershipAdmin(admin.ModelAdmin):
    exclude = BaseLaunchAble.get_exclude_field_names();
admin.site.register(ContextMembership, ContextMembershipAdmin)

class ScoreAdmin(admin.ModelAdmin):
    exclude = BaseLaunchAble.get_exclude_field_names();
admin.site.register(Score, ScoreAdmin)

