# Generated by Django 3.2.8 on 2022-01-02 05:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelSystem', '0025_auto_20211231_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkin',
            name='check_in_date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 2, 13, 17, 29, 835125)),
        ),
        migrations.AlterField(
            model_name='checkin',
            name='last_edited_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 2, 13, 17, 29, 835125)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='expected_arrival_date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 2, 13, 17, 29, 819482)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='expected_departure_date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 2, 13, 17, 29, 819482)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='reservation_date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 2, 13, 17, 29, 819482)),
        ),
    ]
