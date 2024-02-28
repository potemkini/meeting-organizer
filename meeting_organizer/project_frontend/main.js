let allActiveMeetingsArray = []
let allUsersArray = []
let selectedParticipants = [];

const meeting_detail_container = document.querySelector(".meeting-detail-container");
const create_meeting_container = document.querySelector(".create-meeting-container");


window.onload = async function () { 
    await setCookie();
    fetchAllActiveMeetingsAndUsers(); 
    
};
    
document.addEventListener('keypress', function (e) {
    if (e.keyCode === 13 || e.which === 13) {
        e.preventDefault();
        return false;
    }
});


async function setCookie() {
    const response = await fetch("http://127.0.0.1:8000/api-v1/set-csrf-cookie");
    const data = await response.json();
    console.log(data);
}

async function fetchAllActiveMeetingsAndUsers() {
    const response = await fetch("http://127.0.0.1:8000/api-v1/active-meetings-and-users");
    const data = await response.json();
    const fetchedActiveMeetingsArray = data.all_active_meetings;
    const fetchedAllUsersArray = data.all_users;
    allActiveMeetingsArray = fetchedActiveMeetingsArray
    allUsersArray = fetchedAllUsersArray
    
    for (var i = 0; i < allActiveMeetingsArray.length; i++) {
        document.getElementById("active-meetings-list").innerHTML += "<li onclick='fetchMeetingDetail(" + allActiveMeetingsArray[i].id + ")'><a>Meeting Code: <strong class='meeting-code-hover'>" + allActiveMeetingsArray[i].meeting_code + "</strong></a></li>";
    }

    
    for (var i = 0; i < allUsersArray.length; i++) {
        if (allUsersArray[i].name != "Manager") {
            document.querySelector(".participant-form-select").innerHTML += "<option value='" + allUsersArray[i].id + "'>"+ allUsersArray[i].name +"</option>";
        }
            
    }

}

function fetchMeetingDetail(meetingId) {
    document.getElementById("selected-meeting-detail").innerHTML = "";
    document.getElementById("participant-list").innerHTML = "";
    document.getElementById("participants-count").innerHTML = "";
    document.getElementById("delete-participant-box").innerHTML = "";
    document.getElementById("update-participant-box").innerHTML = "";

    const targetMeetingArray = allActiveMeetingsArray.filter((item) => item.id == meetingId)[0];
    const participantsOfMeetingArray = targetMeetingArray.participants;
    create_meeting_container.classList.add("is-hidden");
    meeting_detail_container.classList.remove("is-hidden");

    
    document.getElementById("participants-count").innerHTML += participantsOfMeetingArray.length

    document.getElementById("selected-meeting-detail").innerHTML += "<li ><a>Meeting Code: <strong>" + targetMeetingArray.meeting_code + "</strong></a></li>";
    document.getElementById("selected-meeting-detail").innerHTML += "<li ><a>Topic: <strong contenteditable='true' id='update_topic'>" + targetMeetingArray.topic + "</strong></a></li>";
    document.getElementById("selected-meeting-detail").innerHTML += "<li ><a>Meeting Day: <strong contenteditable='true' id='update_meeting_day'>" + targetMeetingArray.meeting_day + "</strong></a></li>";
    document.getElementById("selected-meeting-detail").innerHTML += "<li ><a>Starting Time: <strong contenteditable='true' id='update_starting_time'>" + targetMeetingArray.start_time + "</strong></a></li>";
    document.getElementById("selected-meeting-detail").innerHTML += "<li ><a>End Time: <strong contenteditable='true' id='update_end_time'>" + targetMeetingArray.end_time + "</strong></a></li>";
    document.getElementById("selected-meeting-detail").innerHTML += "<li ><a>Created By: <strong>" + targetMeetingArray.created_by + "</strong></a></li>";
    for (var i = 0; i < participantsOfMeetingArray.length; i++) {
        document.getElementById("participant-list").innerHTML += "<li><a>" + participantsOfMeetingArray[i] + "</a></li>";
    }
    document.getElementById("delete-participant-box").innerHTML += "<button class='button is-danger is-active' onclick='deleteMeeting(" + targetMeetingArray.id + ")'>Delete</button>";
    document.getElementById("update-participant-box").innerHTML += "<button class='button is-warning is-active' onclick='updateMeeting(" + targetMeetingArray.id + ")'>Update</button>";
    
}



async function openCreateMeetingContainer() {
    create_meeting_container.classList.remove("is-hidden");
    meeting_detail_container.classList.add("is-hidden");
    const partipicantFormSelect = document.querySelector('.participant-form-select');

    partipicantFormSelect.addEventListener('change', function () {


        if (selectedParticipants.includes(this.value)) {
            var index_of_existing_participant = selectedParticipants.indexOf(this.value);
            if (index_of_existing_participant !== -1) {
                selectedParticipants.splice(index_of_existing_participant, 1);
                this.options[this.selectedIndex].style.backgroundColor = "#ffffff";
                this.options[this.selectedIndex].style.color = "#000000";

                
            }
        } else {
            this.options[this.selectedIndex].style.backgroundColor = "#00d1b2";
            this.options[this.selectedIndex].style.color = "#ffffff";
            selectedParticipants.push(this.value);
        }
    });
    
    
}

   
 
async function createMeeting() {
    let host = document.getElementById("host").value
    let topic = document.getElementById("topic").value
    let meeting_day = document.getElementById("meeting_day").value
    let starting_time = document.getElementById("starting_time").value
    let end_time = document.getElementById("end_time").value

    const post_data = {
        "host": host,
        "topic": topic,
        "meeting_day": meeting_day,
        "starting_time": starting_time,
        "end_time": end_time,
        "participants": selectedParticipants
    }

    if (topic == "" || meeting_day == "" || starting_time == "" || end_time == "") {
        alert("Please fill all fields")
        return
    }

    let response = await fetch("http://127.0.0.1:8000/api-v1/create-meeting", {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(post_data),
    })

    if (response.status == 200 ) {
        console.log(response.message)
    } else {
        console.log(response.message)
        window.location.reload()

    }

};

async function updateMeeting(meeting_id) {
    let topic = document.getElementById("update_topic").textContent
    let meeting_day = document.getElementById("update_meeting_day").textContent
    let starting_time = document.getElementById("update_starting_time").textContent
    let end_time = document.getElementById("update_end_time").textContent

    const post_data = {
        "topic": topic.replace(/^\s+|\s+$/gm, ''),
        "meeting_day": meeting_day.replace(/^\s+|\s+$/gm, ''),
        "starting_time": starting_time.replace(/^\s+|\s+$/gm, ''),
        "end_time": end_time.replace(/^\s+|\s+$/gm, ''),
    }


    if (topic == "" || meeting_day == "" || starting_time == "" || end_time == "") {
        alert("Please fill all fields")
        return
    }

    console.log(post_data)
    

    let response = await fetch("http://127.0.0.1:8000/api-v1/update-meeting/" + meeting_id, {
        method: 'PUT',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(post_data),
    })

    if (response.status == 200) {
        console.log(response.message)
    } else {
        console.log(response.message)
        window.location.reload()

    }


}

async function deleteMeeting(meeting_id) {
    let response = await fetch("http://127.0.0.1:8000/api-v1/delete-meeting/" + meeting_id, {
        method: 'DELETE',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: null,
    })

    if (response.status == 200) {
        console.log(response.message)
        // window.location.reload()
    }

}
