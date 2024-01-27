from django.contrib import admin

from .models import BaseLTI, Tenant, Context, Subject, Link, LineItem, Membership, Score, ContextLog

class TenantAdmin(admin.ModelAdmin):
    exclude = BaseLTI.get_exclude_field_names();
admin.site.register(Tenant, TenantAdmin)

class ContextAdmin(admin.ModelAdmin):
    exclude = BaseLTI.get_exclude_field_names();
admin.site.register(Context, ContextAdmin)

class SubjectAdmin(admin.ModelAdmin):
    exclude = BaseLTI.get_exclude_field_names();
admin.site.register(Subject, SubjectAdmin)

class LinkAdmin(admin.ModelAdmin):
    exclude = BaseLTI.get_exclude_field_names();
admin.site.register(Link, LinkAdmin)

class LineItemAdmin(admin.ModelAdmin):
    exclude = BaseLTI.get_exclude_field_names();
admin.site.register(LineItem, LineItemAdmin)

class MembershipAdmin(admin.ModelAdmin):
    exclude = BaseLTI.get_exclude_field_names();
admin.site.register(Membership, MembershipAdmin)

class ScoreAdmin(admin.ModelAdmin):
    exclude = BaseLTI.get_exclude_field_names();
admin.site.register(Score, ScoreAdmin)

admin.site.register(ContextLog)

