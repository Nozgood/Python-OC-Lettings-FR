# Generated by Django 3.0 on 2024-06-05 05:37

from django.db import migrations


def transfer_profile_data(apps, schema_editor):
    old_profile = apps.get_model('oc_lettings_site', 'Profile')
    new_profile = apps.get_model('profiles', 'Profile')
    user = apps.get_model('auth', 'User')

    user_map = {user.id: user for user in user.objects.all()}

    for old_profile in old_profile.objects.all():
        user = user_map[old_profile.user_id]
        new_profile.objects.create(
            user=user,
            favorite_city=old_profile.favorite_city
        )


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.RunPython(transfer_profile_data),
    ]