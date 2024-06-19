from django.test import TestCase
from lettings.models import Address


class AddressModelTest(TestCase):

    def test_address_creation(self):
        address = Address.objects.create(
            number=123,
            street='Main St',
            city='Test City',
            state='TC',
            zip_code=12345,
            country_iso_code='TST'
        )
        self.assertEqual(address.number, 123)
        self.assertEqual(address.street, 'Main St')
        self.assertEqual(address.city, 'Test City')
        self.assertEqual(address.state, 'TC')
        self.assertEqual(address.zip_code, 12345)
        self.assertEqual(address.country_iso_code, 'TST')

    def test_address_str(self):
        address = Address.objects.create(
            number=123,
            street='Main St',
            city='Test City',
            state='TC',
            zip_code=12345,
            country_iso_code='TST'
        )
        self.assertEqual(str(address), '123 Main St')