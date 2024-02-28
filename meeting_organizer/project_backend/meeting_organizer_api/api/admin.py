from django.contrib import admin
from api.models import Meeting, Participants
# Register your models here.




class AdminMeeting(admin.ModelAdmin):
    list_display = ('topic', 'meeting_day', 'meeting_code', 'active')
    ordering = ('-created_date',)
    filter_horizontal = ('participants',)
admin.site.register(Meeting, AdminMeeting)

class AdminParticipants(admin.ModelAdmin):
    list_display = ('name', 'email')
admin.site.register(Participants, AdminParticipants)