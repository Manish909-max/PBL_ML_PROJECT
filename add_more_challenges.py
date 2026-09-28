import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_mock_interview.settings')
django.setup()

from interviews.models import CodingChallenge, DailyChallenge
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()
admin_user = User.objects.filter(is_superuser=True).first()

c1 = CodingChallenge.objects.create(
    title='Aptitude: Age Problem',
    description='A father is twice as old as his son. 20 years ago, the age of the father was 12 times the age of the son. What is the present age of the father?',
    explanation='Let son=x, father=2x. 20 years ago: 2x - 20 = 12(x - 20). 2x - 20 = 12x - 240. 10x = 220 -> x = 22. Father is 2x = 44.',
    test_cases=[{'option': '32'}, {'option': '44'}, {'option': '54'}, {'option': '60'}],
    expected_keywords='44',
    difficulty='medium',
    timer_minutes=10,
    created_by=admin_user,
    is_active=True
)

c2 = CodingChallenge.objects.create(
    title='Aptitude: Time and Work',
    description='A can do a work in 15 days and B in 20 days. If they work on it together for 4 days, then the fraction of the work that is left is:',
    explanation='A\'s 1 day work = 1/15, B\'s 1 day work = 1/20. Together they do (1/15 + 1/20) = 7/60 of the work in 1 day. In 4 days, they complete 28/60 = 7/15. Fraction left = 1 - 7/15 = 8/15.',
    test_cases=[{'option': '1/4'}, {'option': '1/10'}, {'option': '7/15'}, {'option': '8/15'}],
    expected_keywords='8/15',
    difficulty='hard',
    timer_minutes=15,
    created_by=admin_user,
    is_active=True
)

c3 = CodingChallenge.objects.create(
    title='Aptitude: Simple Interest',
    description='A sum of money at simple interest amounts to $815 in 3 years and to $854 in 4 years. The sum is:',
    explanation='Interest for 1 year = 854 - 815 = $39. Interest for 3 years = 39 * 3 = $117. Sum (Principal) = 815 - 117 = $698.',
    test_cases=[{'option': '650'}, {'option': '690'}, {'option': '698'}, {'option': '700'}],
    expected_keywords='698',
    difficulty='easy',
    timer_minutes=10,
    created_by=admin_user,
    is_active=True
)

c4 = CodingChallenge.objects.create(
    title='Logical Reasoning: Missing Number',
    description='Find the missing number in the sequence: 2, 6, 12, 20, 30, 42, 56, ?',
    explanation='The pattern is adding consecutive even numbers: +4, +6, +8, +10, +12, +14, +16. Therefore, 56 + 16 = 72. Alternatively, n*(n+1): 1*2, 2*3, 3*4... 8*9 = 72.',
    test_cases=[{'option': '68'}, {'option': '72'}, {'option': '80'}, {'option': '90'}],
    expected_keywords='72',
    difficulty='easy',
    timer_minutes=5,
    created_by=admin_user,
    is_active=True
)

c5 = CodingChallenge.objects.create(
    title='Logical Reasoning: Blood Relations',
    description='Pointing to a photograph of a boy Suresh said, "He is the son of the only son of my mother." How is Suresh related to that boy?',
    explanation='Suresh\'s mother\'s only son is Suresh himself. The boy in the photograph is the son of Suresh. Therefore, Suresh is the father of the boy.',
    test_cases=[{'option': 'Brother'}, {'option': 'Uncle'}, {'option': 'Father'}, {'option': 'Cousin'}],
    expected_keywords='Father',
    difficulty='medium',
    timer_minutes=10,
    created_by=admin_user,
    is_active=True
)

today = timezone.now().date()
dc, created = DailyChallenge.objects.get_or_create(date=today, defaults={'created_by': admin_user})

# Add all aptitude challenges to the daily rotation
old_challenges = CodingChallenge.objects.filter(is_active=True, title__icontains='Aptitude')
dc.challenges.add(c1, c2, c3, c4, c5)
for c in old_challenges:
    dc.challenges.add(c)
    
print('Successfully added more questions and updated the daily rotation!')
