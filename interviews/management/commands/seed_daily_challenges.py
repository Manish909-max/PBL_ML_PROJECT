from django.core.management.base import BaseCommand
from interviews.models import CodingChallenge
from users.models import User


class Command(BaseCommand):
    help = 'Seed daily challenges with easy, medium, and hard problems'

    def handle(self, *args, **options):
        # Get or create a system admin for created_by
        admin_user, _ = User.objects.get_or_create(
            username='system_admin',
            defaults={'email': 'admin@system.local', 'is_staff': True, 'is_superuser': True}
        )

        challenges = [
            {
                'title': 'Two Sum',
                'description': 'Given an array of integers nums and an integer target, return the indices of the two numbers that add up to target.\n\nYou may assume that each input has exactly one solution, and you may not use the same element twice.\n\nExample:\nInput: nums = [2,7,11,15], target = 9\nOutput: [0,1]\nExplanation: nums[0] + nums[1] == 9, so we return [0, 1].',
                'starter_code': '''from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # HINT: Use a hash map to store values you've seen
        # For each number, check if (target - number) exists in the map
        pass''',
                'expected_keywords': 'hash,map,complement,enumerate',
                'difficulty': 'easy',
                'timer_minutes': 60,
                'test_cases': [
                    {'input': '[2,7,11,15], 9', 'output': '[0,1]'},
                    {'input': '[3,2,4], 6', 'output': '[1,2]'},
                    {'input': '[3,3], 6', 'output': '[0,1]'},
                    {'input': '[1,2,3,4,5], 9', 'output': '[3,4]'},
                ],
            },
            {
                'title': 'Reverse Integer',
                'description': 'Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.\n\nAssume the environment does not allow you to store 64-bit integers (signed or unsigned).\n\nExample:\nInput: x = 123\nOutput: 321\n\nInput: x = -123\nOutput: -321\n\nInput: x = 120\nOutput: 21',
                'starter_code': '''class Solution:
    def reverse(self, x: int) -> int:
        # TODO: Reverse the digits of the integer
        # Handle negative numbers and overflow conditions
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        pass''',
                'expected_keywords': 'reverse,modulo,digits,overflow,range',
                'difficulty': 'medium',
                'timer_minutes': 60,
                'test_cases': [
                    {'input': '123', 'output': '321'},
                    {'input': '-123', 'output': '-321'},
                    {'input': '120', 'output': '21'},
                    {'input': '0', 'output': '0'},
                    {'input': '1534236469', 'output': '0'},
                ],
            },
            {
                'title': 'Median of Two Sorted Arrays',
                'description': 'Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.\n\nThe overall run time complexity should be O(log (m+n)).\n\nExample:\nInput: nums1 = [1,3], nums2 = [2]\nOutput: 2.0\nExplanation: merged array = [1,2,3] and median is 2.\n\nInput: nums1 = [1,2], nums2 = [3,4]\nOutput: 2.5\nExplanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.',
                'starter_code': '''from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # CHALLENGE: Solve this in O(log(m+n)) time
        # HINT: Use binary search on the smaller array
        # Partition both arrays such that left and right halves have equal elements
        pass''',
                'expected_keywords': 'binary,search,partition,median,log',
                'difficulty': 'hard',
                'timer_minutes': 60,
                'test_cases': [
                    {'input': '[1,3], [2]', 'output': '2.0'},
                    {'input': '[1,2], [3,4]', 'output': '2.5'},
                    {'input': '[0,0], [0,0]', 'output': '0.0'},
                    {'input': '[], [1]', 'output': '1.0'},
                    {'input': '[2], []', 'output': '2.0'},
                ],
            },
        ]

        for challenge_data in challenges:
            challenge, created = CodingChallenge.objects.get_or_create(
                title=challenge_data['title'],
                defaults={
                    'description': challenge_data['description'],
                    'starter_code': challenge_data['starter_code'],
                    'expected_keywords': challenge_data['expected_keywords'],
                    'difficulty': challenge_data['difficulty'],
                    'timer_minutes': challenge_data['timer_minutes'],
                    'test_cases': challenge_data['test_cases'],
                    'is_active': True,
                    'created_by': admin_user,
                }
            )

            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'✓ Created challenge: {challenge.title} ({challenge.get_difficulty_display()})')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'⊘ Challenge already exists: {challenge.title}')
                )

        self.stdout.write(self.style.SUCCESS('✅ Daily challenges seeded successfully!'))
