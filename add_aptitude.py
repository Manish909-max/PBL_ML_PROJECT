import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_mock_interview.settings')
django.setup()

from interviews.models import CodingChallenge, DailyChallenge
from django.contrib.auth import get_user_model
from django.utils import timezone
import json

User = get_user_model()
admin_user = User.objects.filter(is_superuser=True).first()

# Aptitude: Train problem
easy = CodingChallenge.objects.create(
    title='Train Speed and Distance',
    description='A train is moving at a given speed in km/hr. It crosses a pole in a certain number of seconds. Write a function that returns the length of the train in meters (rounded to the nearest integer).\n\nInput format: two numbers separated by a newline. First line: speed in km/hr. Second line: time in seconds.',
    starter_code='speed = int(input())\ntime = int(input())\n\n# Calculate length in meters (rounded to int)\n',
    expected_keywords='print',
    difficulty='easy',
    test_cases=[
        {'input': '60\n9', 'output': '150'},
        {'input': '90\n10', 'output': '250'}
    ],
    timer_minutes=15,
    created_by=admin_user,
    is_active=True
)

# Aptitude: Number Series
medium = CodingChallenge.objects.create(
    title='Number Series: Find the nth Term',
    description='Given a sequence of numbers where each term after the first is the sum of the squares of the digits of the previous term. Given the first term and N, find the Nth term in the sequence.\n\nInput format: First line is the starting term. Second line is N.',
    starter_code='start = int(input())\nn = int(input())\n\n# Find the nth term and print it\n',
    expected_keywords='print',
    difficulty='medium',
    test_cases=[
        {'input': '12\n3', 'output': '25'},
        {'input': '2\n4', 'output': '37'}
    ],
    timer_minutes=25,
    created_by=admin_user,
    is_active=True
)

# Aptitude: Probability
hard = CodingChallenge.objects.create(
    title='Probability: Balls in a Bag',
    description='A bag contains R red balls, G green balls, and B blue balls. Two balls are drawn at random without replacement. Write a program to calculate the exact probability (as a simplified string fraction a/b) that both balls are of the same color.\n\nInput format: Three integers R, G, B each on a new line.',
    starter_code='import math\nr = int(input())\ng = int(input())\nb = int(input())\n\n# Print probability in format "a/b"\n',
    expected_keywords='print',
    difficulty='hard',
    test_cases=[
        {'input': '4\n5\n3', 'output': '19/66'}, 
        {'input': '2\n1\n1', 'output': '1/6'}
    ],
    timer_minutes=45,
    created_by=admin_user,
    is_active=True
)

today = timezone.now().date()
DailyChallenge.create_or_update_today(
    easy=easy,
    medium=medium,
    hard=hard,
    admin_user=admin_user
)
print('Aptitude challenges added!')
