from django.db import models
from datetime import datetime, date, time, timedelta
from django.utils.text import slugify


# Create your models here.

def return_date_time():
    now = datetime.now() + timedelta(hours=3)
    return now

class Participants(models.Model):

    name = models.CharField(null=True, blank=True, max_length=100, verbose_name="Participant Name")
    email = models.EmailField(null=True, blank=True, max_length=100, verbose_name="Participant Email")
    class Meta:
        verbose_name = ("Participant")
        verbose_name_plural = ("Participants")

    def __str__(self):
        return self.name

class Meeting(models.Model):

    topic = models.CharField(null=True, blank=False, max_length=180, verbose_name="Meeting Topic")
    meeting_day = models.DateField(null=True, blank=False, verbose_name="Meeting Day")
    start_time = models.TimeField(null=True, blank=False, verbose_name="Start Time")
    end_time = models.TimeField(null=True, blank=False, verbose_name="End Time")
    participants = models.ManyToManyField(Participants, related_name="participants", blank=True, null=True, verbose_name="Participants")
    created_by = models.ForeignKey(Participants, on_delete=models.SET_NULL, blank=False, null=True, related_name="created_by" ,verbose_name="Created By")
    created_date = models.DateTimeField(default=return_date_time, verbose_name="Created Date")
    meeting_code = models.CharField(unique=True, null=True, max_length=100, blank=True, editable=False)
    active = models.BooleanField(default=True, verbose_name="Active")

    def save(self, *args, **kwargs):
        self.meeting_code = str(self.created_date.timestamp()).split('.')[0]
        super(Meeting, self).save(*args, **kwargs)


    class Meta:
        verbose_name = ("Meeting")
        verbose_name_plural = ("Meetings")


    def __str__(self):
        return self.topic
