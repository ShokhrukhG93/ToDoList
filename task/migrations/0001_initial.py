# Generated by Django 5.0.4 on 2024-06-25 13:18

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('date', models.DateTimeField(default=datetime.datetime(2024, 6, 25, 18, 18, 38, 38699))),
                ('completed', models.BooleanField(default=False)),
                ('type', models.CharField(choices=[('E', 'Event'), ('T', 'Task'), ('A', 'Appointment schedule')], max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
