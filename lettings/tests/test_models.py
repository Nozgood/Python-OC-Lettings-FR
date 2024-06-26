from django.test import TestCase
from lettings.models import Address, Letting


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


class LettingModelTest(TestCase):

    def setUp(self):
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

    def test_letting_creation(self):
        self.assertEqual(self.letting.title, 'Test Leting')
        self.assertEqual(self.letting.address, self.address)

    def test_letting_str(self):
        self.assertEqual(str(self.letting), 'Test Letting')

    def test_letting_address_cascade_delete(self):
        self.address.delete()
        lettings = Letting.objects.filter(title='Test Letting')
        self.assertEqual(lettings.count(), 0)
