from django.core.management.base import BaseCommand

from interviews.models import Interview, Question


class Command(BaseCommand):
    help = 'Seed default interview templates for the AI Mock Interview Assistant.'

    def handle(self, *args, **options):
        defaults = [
            {
                'title': 'Backend Development Interview',
                'topic': 'backend',
                'difficulty': 'medium',
                'duration_minutes': 30,
                'questions': [
                    'Explain how you would design a scalable REST API for a high-traffic service.',
                    'How do you ensure database consistency and handle concurrency issues?',
                ],
            },
            {
                'title': 'Data Science Interview',
                'topic': 'data_science',
                'difficulty': 'hard',
                'duration_minutes': 45,
                'questions': [
                    'Describe a time you used feature engineering to improve a model.',
                    'How do you evaluate model drift and production performance?',
                ],
            },
            {
                'title': 'Frontend Interview',
                'topic': 'frontend',
                'difficulty': 'medium',
                'duration_minutes': 35,
                'questions': [
                    'How do you optimize UI performance for large data-heavy dashboards?',
                    'Explain your approach to accessible and responsive component design.',
                ],
            },
            {
                'title': 'DevOps Interview',
                'topic': 'devops',
                'difficulty': 'hard',
                'duration_minutes': 40,
                'questions': [
                    'How would you design a CI/CD pipeline for a microservices platform?',
                    'What monitoring and incident response strategy do you use?',
                ],
            },
        ]

        for data in defaults:
            interview, created = Interview.objects.get_or_create(
                title=data['title'],
                defaults={
                    'topic': data['topic'],
                    'difficulty': data['difficulty'],
                    'duration_minutes': data['duration_minutes'],
                    'status': 'active',
                },
            )
            if created:
                for index, question_text in enumerate(data['questions'], start=1):
                    Question.objects.get_or_create(
                        interview=interview,
                        order=index,
                        defaults={'text': question_text, 'expected_duration': 90},
                    )

        self.stdout.write(self.style.SUCCESS(f'Created {Interview.objects.count()} interviews.'))
