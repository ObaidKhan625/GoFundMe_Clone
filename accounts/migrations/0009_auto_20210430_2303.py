# Generated by Django 3.1.4 on 2021-04-30 17:33

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0008_auto_20210430_2257'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='Customers',
        ),
    ]
