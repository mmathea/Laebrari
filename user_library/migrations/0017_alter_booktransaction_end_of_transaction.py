# Generated by Django 3.2.9 on 2022-08-09 19:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_library', '0016_auto_20220808_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booktransaction',
            name='end_of_transaction',
            field=models.DateField(default=datetime.datetime(2022, 8, 9, 19, 0, 2, 889651), verbose_name='return_date'),
            preserve_default=False,
        ),
    ]