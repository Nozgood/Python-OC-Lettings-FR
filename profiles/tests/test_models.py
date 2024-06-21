from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import Profile


class ProfileModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='test',
            password='12345'
        )
        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city='Test City'
        )

    def test_profile_creation(self):
        self.assertEqual(self.profile.user.username, 'test')
        self.assertEqual(self.profile.favorite_city, 'Test City')

    def test_profile_str(self):
        self.assertEqual(str(self.profile), 'test')

    def test_profile_user_cascade_delete(self):
        self.user.delete()
        profiles = Profile.objects.filter(user__username='test')
        self.assertEqual(profiles.count(), 0)
