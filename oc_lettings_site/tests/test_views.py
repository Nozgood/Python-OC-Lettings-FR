from django.test import TestCase
from django.urls import reverse


class IndexViewTest(TestCase):

    def test_index_view(self):
        """
        Test the index view to ensure it returns a 200 status code
        and uses the correct template.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
