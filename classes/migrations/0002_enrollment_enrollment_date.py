# Generated by Django 4.2 on 2023-05-08 16:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='enrollment_date',
            field=models.DateField(default=datetime.date(2023, 5, 8)),
        ),
    ]