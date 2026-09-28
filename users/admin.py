from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.html import format_html
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['username', 'email', 'get_ban_status', 'suspicious_activity_count', 'date_joined']
    list_filter = ['is_banned', 'date_joined', 'is_staff']
    search_fields = ['username', 'email']
    
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Security & Monitoring', {
            'fields': ('is_banned', 'ban_reason', 'banned_at', 'banned_by', 'suspicious_activity_count')
        }),
        ('Camera & Screen', {
            'fields': ('camera_enabled', 'screen_share_enabled')
        }),
        ('Interview Preferences', {
            'fields': ('bio', 'expertise', 'preferred_role')
        }),
    )
    
    readonly_fields = ['banned_at', 'banned_by', 'suspicious_activity_count']
    
    def get_ban_status(self, obj):
        if obj.is_banned:
            return format_html('<span style="color: red;">🚫 Banned</span>')
        return format_html('<span style="color: green;">✅ Active</span>')
    get_ban_status.short_description = 'Ban Status'
    
    actions = ['ban_users', 'unban_users']
    
    def ban_users(self, request, queryset):
        count = queryset.update(is_banned=True, banned_by=request.user)
        self.message_user(request, f'{count} users banned.')
    ban_users.short_description = "Ban selected users"
    
    def unban_users(self, request, queryset):
        count = queryset.update(is_banned=False, ban_reason='', banned_by=None)
        self.message_user(request, f'{count} users unbanned.')
    unban_users.short_description = "Unban selected users"
