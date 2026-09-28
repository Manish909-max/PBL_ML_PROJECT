from django.contrib import admin
from .models import Interview, Question, InterviewSession, CandidateResponse, SuspiciousActivity


@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    list_display = ['title', 'topic', 'difficulty', 'status', 'duration_minutes', 'created_at']
    list_filter = ['topic', 'difficulty', 'status', 'created_at']
    search_fields = ['title']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Basic Info', {'fields': ('title', 'topic', 'difficulty', 'duration_minutes')}),
        ('Status', {'fields': ('status', 'user')}),
        ('Metadata', {'fields': ('created_at', 'updated_at')}),
    )


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'interview', 'order', 'expected_duration', 'created_at']
    list_filter = ['interview', 'created_at']
    search_fields = ['text', 'interview__title']
    readonly_fields = ['created_at']
    ordering = ['interview', 'order']


@admin.register(InterviewSession)
class InterviewSessionAdmin(admin.ModelAdmin):
    list_display = ['candidate', 'interview_template', 'status', 'score', 'started_at', 'ended_at']
    list_filter = ['status', 'interview_template', 'created_at']
    search_fields = ['candidate__username', 'interview_template__title']
    readonly_fields = ['created_at', 'updated_at', 'started_at', 'ended_at']
    fieldsets = (
        ('Session Info', {'fields': ('candidate', 'interview_template', 'status')}),
        ('Progress', {'fields': ('current_question_order', 'score')}),
        ('Timing', {'fields': ('started_at', 'ended_at', 'created_at', 'updated_at')}),
    )


@admin.register(CandidateResponse)
class CandidateResponseAdmin(admin.ModelAdmin):
    list_display = ['session', 'question', 'confidence_level', 'score', 'created_at']
    list_filter = ['confidence_level', 'session__interview_template', 'created_at']
    search_fields = ['session__candidate__username', 'response_text']
    readonly_fields = ['created_at']
    fieldsets = (
        ('Response', {'fields': ('session', 'question', 'response_text')}),
        ('Assessment', {'fields': ('confidence_level', 'score', 'feedback')}),
        ('Metadata', {'fields': ('created_at',)}),
    )


@admin.register(SuspiciousActivity)
class SuspiciousActivityAdmin(admin.ModelAdmin):
    list_display = ['candidate', 'activity_type', 'severity', 'action_taken', 'reviewed', 'detected_at']
    list_filter = ['activity_type', 'severity', 'action_taken', 'reviewed', 'detected_at']
    search_fields = ['candidate__username', 'description', 'admin_notes']
    readonly_fields = ['detected_at', 'created_at']
    
    fieldsets = (
        ('Incident Info', {'fields': ('candidate', 'session', 'activity_type', 'severity')}),
        ('Details', {'fields': ('description', 'detected_at')}),
        ('Admin Review', {'fields': ('reviewed', 'admin_notes', 'action_taken')}),
        ('Metadata', {'fields': ('created_at',)}),
    )
    
    actions = ['mark_reviewed', 'ban_account']
    
    def mark_reviewed(self, request, queryset):
        queryset.update(reviewed=True)
    mark_reviewed.short_description = "Mark selected as reviewed"
    
    def ban_account(self, request, queryset):
        for activity in queryset:
            activity.candidate.ban_account(request.user, f"Banned due to {activity.activity_type}")
            activity.action_taken = 'banned'
            activity.save()
    ban_account.short_description = "Ban accounts for selected activities"

