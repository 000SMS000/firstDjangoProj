from django.shortcuts import render

def index(request):
    context = {
        "full_name": "SMS",
        "student_id": "120210278",
        "address": "Gaza, Palestine",
        "email": "SMS@gmail.com",
        "extra_info": "Student in IUG"
    }
    return render(request, 'pages/index.html', context)
