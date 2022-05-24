# Generated by Django 3.2.9 on 2022-05-24 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_library', '0002_auto_20220524_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='librarian',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='librarian',
            name='can_loan',
            field=models.BooleanField(default=False, verbose_name='Can loan a book'),
        ),
        migrations.AlterField(
            model_name='librarian',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='librarian',
            name='phone_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
