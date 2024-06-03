from models import Letting as OCLetting
from models import Address as OCAddress
from lettings.models import Letting
from lettings.models import Address


def migrate_addresses():
    oc_table_addresses_objects = OCAddress.objects.all()
    for entry in oc_table_addresses_objects:
        Address.objects.create(
            number=entry.number,
            street=entry.street,
            city=entry.city,
            state=entry.state,
            zip_code=entry.zip_code,
            country_iso_code=entry.country_iso_code
        )
        return print("migration for addresses correctly done")


def migrate_lettings():
    oc_table_letting_objects = OCLetting.objects.all()
    for entry in oc_table_letting_objects:
        Letting.objects.create(
            title=entry.title,
            address=entry.address
        )
        return print("migration for lettings correctly done")
