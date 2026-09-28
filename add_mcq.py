import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_mock_interview.settings')
django.setup()

from interviews.models import CodingChallenge
import json

for c in CodingChallenge.objects.all():
    if 'Train' in c.title:
        # Expected is 150
        c.test_cases = [{'option': '100'}, {'option': '125'}, {'option': '150'}, {'option': '175'}]
        c.expected_keywords = '150'
        c.save()
    elif 'Probability' in c.title:
        # Expected is 19/66
        c.test_cases = [{'option': '1/6'}, {'option': '19/66'}, {'option': '1/3'}, {'option': '2/11'}]
        c.expected_keywords = '19/66'
        c.save()
    elif 'Number Series' in c.title:
        # Expected is 25
        c.test_cases = [{'option': '15'}, {'option': '25'}, {'option': '37'}, {'option': '41'}]
        c.expected_keywords = '25'
        c.save()

print('Updated challenges to MCQ')
