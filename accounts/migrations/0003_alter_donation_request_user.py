# Generated by Django 4.0.1 on 2022-01-07 14:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_donation_made_donation_request_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation_request',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_donation_request', to=settings.AUTH_USER_MODEL),
        ),
    ]