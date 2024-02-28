# Generated by Django 4.2.10 on 2024-02-27 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Participant Name')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='Participant Email')),
            ],
            options={
                'verbose_name': 'Participant',
                'verbose_name_plural': 'Participants',
            },
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.TextField(blank=True, max_length=100, null=True, verbose_name='Meeting Topic')),
                ('meeting_day', models.DateField(blank=True, null=True, verbose_name='Meeting Day')),
                ('start_time', models.TimeField(blank=True, null=True, verbose_name='Start Time')),
                ('end_time', models.TimeField(blank=True, null=True, verbose_name='End Time')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('participants', models.ManyToManyField(to='api.participants', verbose_name='Participants')),
            ],
            options={
                'verbose_name': 'Meeting',
                'verbose_name_plural': 'Meetings',
            },
        ),
    ]