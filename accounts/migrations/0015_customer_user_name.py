# Generated by Django 3.1.4 on 2021-05-01 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20210501_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='user_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
