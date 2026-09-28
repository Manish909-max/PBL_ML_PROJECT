from django.test import TestCase
from django.contrib.auth import get_user_model


class UserModelTests(TestCase):
    def test_custom_user_can_be_created(self):
        user = get_user_model().objects.create_user(
            username='candidate',
            email='candidate@example.com',
            password='SecurePass123!'
        )

        self.assertEqual(user.username, 'candidate')
        self.assertTrue(user.check_password('SecurePass123!'))
        self.assertFalse(user.is_staff)
