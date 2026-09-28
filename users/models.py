from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    bio = models.TextField(blank=True)
    expertise = models.CharField(max_length=120, blank=True)
    preferred_role = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Security and monitoring
    is_banned = models.BooleanField(default=False, help_text="Ban user from taking interviews")
    ban_reason = models.TextField(blank=True, help_text="Reason for account ban")
    banned_at = models.DateTimeField(null=True, blank=True)
    banned_by = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='banned_users',
        help_text="Admin who banned this user"
    )
    
    # Challenge-specific bans (copy-paste violations)
    challenge_banned = models.BooleanField(default=False, help_text="Ban user from daily challenges")
    challenge_ban_reason = models.TextField(blank=True, help_text="Reason for challenge ban")
    challenge_banned_at = models.DateTimeField(null=True, blank=True)
    challenge_banned_by = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='challenge_banned_users',
        help_text="Admin who banned user from challenges"
    )
    
    # Camera/Screen monitoring
    camera_enabled = models.BooleanField(default=True)
    screen_share_enabled = models.BooleanField(default=True)
    suspicious_activity_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.username
    
    def ban_account(self, admin_user, reason=""):
        from django.utils import timezone

        if self.is_staff:
            return False

        self.is_banned = True
        self.ban_reason = reason
        self.banned_at = timezone.now()
        self.banned_by = admin_user
        self.save()
        return True
    
    def ban_from_challenges(self, admin_user, reason="Multiple copy-paste violations"):
        """Ban user from daily challenges after 3 copy-paste attempts"""
        from django.utils import timezone

        self.challenge_banned = True
        self.challenge_ban_reason = reason
        self.challenge_banned_at = timezone.now()
        self.challenge_banned_by = admin_user
        self.save()
        return True
    
    def unban_from_challenges(self, admin_user):
        """Admin unban user from challenges"""
        from django.utils import timezone

        self.challenge_banned = False
        self.challenge_ban_reason = ""
        self.challenge_banned_at = None
        self.challenge_banned_by = None
        self.save()
        return True
