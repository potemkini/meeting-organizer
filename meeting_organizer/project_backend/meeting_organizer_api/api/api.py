from ninja import NinjaAPI
from django.db.models import Q, F, When, Case, Value, Exists, OuterRef
import json
from django.contrib.auth.models import User
from api.models import *
from django.http import *
from django.views.decorators.csrf import ensure_csrf_cookie
import decimal
from decimal import Decimal
# from api.schemes import *
from ninja import Field, Schema

project_api = NinjaAPI()



@ensure_csrf_cookie
@project_api.get('/set-csrf-cookie')
def set_csrf_token(request):
    """
    This will be `/api-v1/set-csrf-cookie/` on `urls.py`
    """
    return JsonResponse({"details": "CSRF cookie set"})


@project_api.get('/active-meetings-and-users')
def active_meetings_and_users(request):

    ## As a starting point; all active meetings and users are fetched
    
    all_active_meetings = Meeting.objects.filter(active=True)
    all_active_meetings_array = []
    for item in all_active_meetings:
        meeting_participants = item.participants.all()
        all_active_meetings_array.append({
            "id": item.id,
            "topic": item.topic,
            "meeting_day": item.meeting_day,
            "start_time": item.start_time.replace(second=0, microsecond=0),
            "end_time": item.end_time.replace(second=0, microsecond=0),
            "meeting_code": item.meeting_code,
            "participants": list(meeting_participants.values_list('name', flat=True)),
            "created_by": item.created_by.name,
        })

    all_users = Participants.objects.all()
    all_users_array = []
    for item in all_users:
        all_users_array.append({
            "id": item.id,
            "name": item.name,
            "email": item.email
        })

    return 200, {
        "success": True,
        "all_active_meetings": all_active_meetings_array,
        "all_users": all_users_array
    }


@project_api.post('/create-meeting')
def create_meeting(request):

    post_data = json.loads(request.body)

    host = post_data['host']
    topic = post_data['topic']
    meeting_day = post_data['meeting_day']
    starting_time = post_data['starting_time']
    end_time = post_data['end_time']
    participants = post_data['participants']

    try:
        created_by = Participants.objects.get(name=host)
    except:
        return 400, {
            "success": False,
            "message": "Host not found"
        }

    new_meeting = Meeting(
        topic=topic,
        meeting_day=meeting_day,
        start_time=starting_time,
        end_time=end_time,
        created_by=created_by,
    )



    new_meeting.save()

    for participant_id in participants:
        picked_participant = Participants.objects.get(id=participant_id)
        new_meeting.participants.add(picked_participant)
    


    new_meeting_array = []
    new_meeting_participants = new_meeting.participants.all()

    new_meeting_array.append({
        "id": new_meeting.id,
        "topic": new_meeting.topic,
        "meeting_day": new_meeting.meeting_day,
        "start_time": new_meeting.start_time.replace(second=0, microsecond=0),
        "end_time": new_meeting.end_time.replace(second=0, microsecond=0),
        "meeting_code": new_meeting.meeting_code,
        "participants": list(new_meeting_participants.values_list('name', flat=True)),
        "created_by": new_meeting.created_by.name,
    })



    return 200, {
        "success": True,
        "message": 'New meeting created successfully',
        "new_meeting": new_meeting_array
    }


@project_api.delete('/delete-meeting/{meeting_id}')
def delete_meeting(request, meeting_id):
    target_meeting = Meeting.objects.get(id=meeting_id)
    target_meeting.delete()
    return 200, {
        "success": True,
        "message": 'The meeting has been deleted successfully',
    }

@project_api.put('/update-meeting/{meeting_id}')
def update_meeting(request, meeting_id):

    post_data = json.loads(request.body)

    topic = post_data['topic']
    meeting_day = post_data['meeting_day']
    starting_time = post_data['starting_time']
    end_time = post_data['end_time']
    try:
        target_meeting = Meeting.objects.get(id=meeting_id)
        target_meeting.topic = topic
        target_meeting.meeting_day = meeting_day
        target_meeting.start_time = starting_time
        target_meeting.end_time = end_time
        target_meeting.save()
        return 200, {
            "success": True,
            "message": 'The meeting has been updated successfully',
        }
    except:
        return 400, {
            "success": False,
            "message": 'An error occurred please try again later',
        }

