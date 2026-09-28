import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_mock_interview.settings')
django.setup()

from interviews.models import CodingChallenge, DailyChallenge
from django.contrib.auth import get_user_model
User = get_user_model()

# Delete existing challenges
CodingChallenge.objects.all().delete()
DailyChallenge.objects.all().delete()

admin_user = User.objects.filter(is_superuser=True).first()

questions = [
    {
        "title": "Aptitude Q1: Train Speed",
        "description": "A train running at the speed of 60 km/hr crosses a pole in 9 seconds. What is the length of the train?",
        "options": ["120 meters", "180 meters", "150 meters", "100 meters"],
        "correct": "150 meters",
        "explanation": "Speed = (60 * 5/18) m/sec = 50/3 m/sec. Length = Speed * Time = (50/3) * 9 = 150 meters.",
        "timer": 1
    },
    {
        "title": "Aptitude Q2: Ratio",
        "description": "If A:B = 2:3 and B:C = 4:5, then C:A is equal to?",
        "options": ["15:8", "12:10", "8:15", "10:12"],
        "correct": "15:8",
        "explanation": "A:B = 2:3, B:C = 4:5. Multiply A:B by 4 and B:C by 3 to equate B. A:B = 8:12, B:C = 12:15. So A:B:C = 8:12:15. C:A = 15:8.",
        "timer": 1
    },
    {
        "title": "Aptitude Q3: Work",
        "description": "A can do a work in 15 days and B in 20 days. If they work on it together for 4 days, then the fraction of the work that is left is:",
        "options": ["1/4", "1/10", "7/15", "8/15"],
        "correct": "8/15",
        "explanation": "A's 1 day work = 1/15. B's 1 day work = 1/20. (A+B)'s 1 day work = 1/15 + 1/20 = 7/60. Work done in 4 days = 4 * (7/60) = 7/15. Work left = 1 - 7/15 = 8/15.",
        "timer": 1
    },
    {
        "title": "Aptitude Q4: Mixture",
        "description": "A mixture contains alcohol and water in the ratio 4:3. If 5 liters of water is added to the mixture, the ratio becomes 4:5. Find the quantity of alcohol in the given mixture.",
        "options": ["10 liters", "12 liters", "15 liters", "20 liters"],
        "correct": "10 liters",
        "explanation": "Let alcohol be 4x and water be 3x. (4x) / (3x + 5) = 4/5. 20x = 12x + 20 => 8x = 20 => x = 2.5. Alcohol = 4x = 10 liters.",
        "timer": 1
    },
    {
        "title": "Aptitude Q5: Simple Interest",
        "description": "A sum of money at simple interest amounts to Rs. 815 in 3 years and to Rs. 854 in 4 years. The sum is:",
        "options": ["Rs. 650", "Rs. 698", "Rs. 700", "Rs. 690"],
        "correct": "Rs. 698",
        "explanation": "S.I. for 1 year = 854 - 815 = Rs. 39. S.I. for 3 years = 39 * 3 = Rs. 117. Principal = 815 - 117 = Rs. 698.",
        "timer": 1
    },
    {
        "title": "Aptitude Q6: Number Series",
        "description": "Look at this series: 2, 1, (1/2), (1/4), ... What number should come next?",
        "options": ["(1/3)", "(1/8)", "(2/8)", "(1/16)"],
        "correct": "(1/8)",
        "explanation": "Each number is half of the previous number.",
        "timer": 1
    },
    {
        "title": "Aptitude Q7: Profit and Loss",
        "description": "Alfred buys an old scooter for Rs. 4700 and spends Rs. 800 on its repairs. If he sells the scooter for Rs. 5800, his gain percent is:",
        "options": ["4 4/7 %", "5 5/11 %", "10 %", "12 %"],
        "correct": "5 5/11 %",
        "explanation": "Total CP = 4700 + 800 = 5500. SP = 5800. Gain = 5800 - 5500 = 300. Gain % = (300/5500) * 100 = 60/11 = 5 5/11 %.",
        "timer": 1
    },
    {
        "title": "Aptitude Q8: Time and Distance",
        "description": "A person crosses a 600 m long street in 5 minutes. What is his speed in km per hour?",
        "options": ["3.6", "7.2", "8.4", "10"],
        "correct": "7.2",
        "explanation": "Speed = 600 / (5 * 60) = 2 m/sec. In km/hr = 2 * (18/5) = 36/5 = 7.2 km/hr.",
        "timer": 1
    },
    {
        "title": "Aptitude Q9: Average",
        "description": "The average of first 50 natural numbers is:",
        "options": ["25.30", "25.5", "25.00", "12.25"],
        "correct": "25.5",
        "explanation": "Sum of first 50 natural numbers = (50 * 51) / 2 = 1275. Average = 1275 / 50 = 25.5.",
        "timer": 1
    },
    {
        "title": "Aptitude Q10: Probability",
        "description": "Tickets numbered 1 to 20 are mixed up and then a ticket is drawn at random. What is the probability that the ticket drawn has a number which is a multiple of 3 or 5?",
        "options": ["1/2", "2/5", "8/15", "9/20"],
        "correct": "9/20",
        "explanation": "Multiples of 3 are: {3, 6, 9, 12, 15, 18}. Multiples of 5 are {5, 10, 15, 20}. Total unique multiples = 9. Probability = 9/20.",
        "timer": 1
    }
]

for idx, q in enumerate(questions):
    CodingChallenge.objects.create(
        title=q["title"],
        description=q["description"],
        test_cases=[{"option": opt} for opt in q["options"]],
        expected_keywords=q["correct"],
        explanation=q["explanation"],
        timer_minutes=q["timer"],
        difficulty="easy",
        is_active=True,
        created_by=admin_user
    )

print(f'Successfully created {len(questions)} aptitude questions.')
