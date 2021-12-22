# Generated by Django 3.1.4 on 2021-06-09 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0027_auto_20210607_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='profile_pic',
        ),
        migrations.AddField(
            model_name='customer',
            name='image_extension',
            field=models.CharField(default='.jpg', max_length=4),
        ),
        migrations.AddField(
            model_name='customer',
            name='random_image_number',
            field=models.CharField(default='2321815', max_length=7),
        ),
        migrations.AlterField(
            model_name='donation_request',
            name='random_image_number',
            field=models.CharField(default='3024808', max_length=7),
        ),
    ]