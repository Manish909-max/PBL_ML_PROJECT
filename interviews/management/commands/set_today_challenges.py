from django.core.management.base import BaseCommand
from django.utils import timezone
from interviews.models import CodingChallenge, DailyChallenge
from users.models import User


class Command(BaseCommand):
    help = 'Set today\'s challenges if not already set'

    def handle(self, *args, **options):
        today = timezone.now().date()
        
        # Check if today's challenges are already set
        existing = DailyChallenge.objects.filter(date=today).first()
        if existing:
            self.stdout.write(
                self.style.WARNING(f'⊘ Today\'s challenges already set: Easy: {existing.easy_challenge.title if existing.easy_challenge else "None"}, Medium: {existing.medium_challenge.title if existing.medium_challenge else "None"}, Hard: {existing.hard_challenge.title if existing.hard_challenge else "None"}')
            )
            return
        
        # Get system admin
        admin_user = User.objects.filter(is_superuser=True).first()
        
        if not admin_user:
            self.stdout.write(
                self.style.ERROR('✗ No admin user found. Please create a superuser first.')
            )
            return
        
        # Get or create one challenge of each difficulty
        easy = CodingChallenge.objects.filter(difficulty='easy', is_active=True).order_by('created_at').first()
        medium = CodingChallenge.objects.filter(difficulty='medium', is_active=True).order_by('created_at').first()
        hard = CodingChallenge.objects.filter(difficulty='hard', is_active=True).order_by('created_at').first()
        
        if not easy or not medium or not hard:
            self.stdout.write(
                self.style.ERROR('✗ Not all difficulty levels have challenges available. Please create challenges first.')
            )
            return
        
        # Create today's rotation
        daily = DailyChallenge.create_or_update_today(
            easy=easy,
            medium=medium,
            hard=hard,
            admin_user=admin_user
        )
        
        self.stdout.write(
            self.style.SUCCESS(f'✅ Today\'s challenges set successfully!')
        )
        self.stdout.write(f'   🟢 Easy: {easy.title}')
        self.stdout.write(f'   🟡 Medium: {medium.title}')
        self.stdout.write(f'   🔴 Hard: {hard.title}')
