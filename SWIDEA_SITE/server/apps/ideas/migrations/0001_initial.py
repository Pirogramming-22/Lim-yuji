# Generated by Django 5.1.4 on 2025-01-15 09:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('devtool', '0002_alter_devtool_kind'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('interest', models.IntegerField(default=0)),
                ('is_starred', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(default='images/default.png', upload_to='images/')),
                ('devtool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devtool.devtool')),
            ],
        ),
    ]
