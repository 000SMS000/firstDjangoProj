from django.shortcuts import render

def index(request):
    context = {
        "full_name": "Your Name",
        "student_id": "12345678",
        "address": "Gaza, Palestine",
        "email": "example@gmail.com",
        "extra_info": "Any additional info you want"
    }
    return render(request, 'pages/index.html', context)
