# Generated by Django 4.2.10 on 2024-02-27 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_meeting_created_by_meeting_meeting_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='meeting_code',
            field=models.CharField(blank=True, editable=False, max_length=100, null=True, unique=True),
        ),
    ]