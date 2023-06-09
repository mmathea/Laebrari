# Generated by Django 3.2.14 on 2023-03-14 19:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_library', '0004_userlibrary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='book title')),
                ('author', models.CharField(max_length=255, verbose_name='author')),
                ('memo', models.CharField(max_length=255, verbose_name='memo')),
                ('isbn', models.CharField(max_length=255, verbose_name='isbn')),
                ('date_acquired', models.DateField(verbose_name='date acquired')),
                ('genre', models.CharField(max_length=255)),
                ('available_to_borrow', models.BooleanField(default=False)),
                ('available_to_sell', models.BooleanField(default=False)),
                ('borrowing_price', models.IntegerField()),
                ('selling_price', models.FloatField()),
                ('book_condition', models.CharField(choices=[('NEW', 'NEW'), ('OLD', 'OLD'), ('GOOD CONDITION', 'GOOD CONDITION')], max_length=255)),
                ('library', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='library_book', to='user_library.userlibrary')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='book_owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('title', 'author')},
            },
        ),
    ]
