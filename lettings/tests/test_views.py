from django.test import TestCase
from django.urls import reverse
from lettings.models import Letting, Address


class LettingViewTests(TestCase):

    def setUp(self):
        # Set up the database for tests with one address and one letting
        self.address = Address.objects.create(
            number=123,
            street='Test Street',
            city='Test City',
            state='TS',
            zip_code=12345,
            country_iso_code='TST'
        )
        self.letting = Letting.objects.create(
            title='Test Letting',
            address=self.address
        )

    def test_index_view(self):
        """
        Test the index view to ensure it returns a 200 status code
        and uses the correct template.
        """
        response = self.client.get(reverse('lettings:lettings_index'))
        print(f"response: {response}")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/index.html')
        self.assertContains(response, 'Test Letting')

    def test_letting_view(self):
        """
        Test the letting view to ensure it returns a 200 status code
        and uses the correct template.
        """
        response = self.client.get(
            reverse('lettings:letting', args=[self.letting.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/letting.html')
        self.assertContains(response, 'Test Letting')
        self.assertContains(response, 'Test Street')