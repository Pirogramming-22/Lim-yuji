# Generated by Django 5.1.4 on 2025-01-09 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='actors',
        ),
        migrations.RemoveField(
            model_name='review',
            name='director',
        ),
        migrations.RemoveField(
            model_name='review',
            name='running_time',
        ),
    ]
