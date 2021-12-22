# Generated by Django 3.1.4 on 2021-05-15 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_auto_20210512_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation_request',
            name='amount_received',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='donation_request',
            name='short_description',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
    ]
