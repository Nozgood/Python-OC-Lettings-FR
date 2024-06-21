from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile


class ProfileViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='test',
            password='12345'
        )
        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city='Test City'
        )

    def test_index_view(self):
        """
        Test the index view to ensure it returns a 200 status code
        and uses the correct template.
        """
        response = self.client.get(reverse('profiles:profiles_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/index.html')
        self.assertContains(response, 'test')

    def test_profile_view(self):
        """
        Test the profile view to ensure it returns a 200 status code
        and uses the correct template.
        """
        response = self.client.get(
            reverse('profiles:profile', args=[self.user.username])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
        self.assertContains(response, 'test')
        self.assertContains(response, 'Test City')
