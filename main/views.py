from django.shortcuts import render

from main.models import Experience, Project

# mengirim data ke index.html
def show_main(request):
    context = {
        "nameCard": "AlyaTsbt",
        "name": "Alya Tsabita Imani",
        "npm": "2506620192",
        "study_program": "Information System",
        "bio": (
            "A diligent and dedicated person with a deep interest in digital products design. " 
            "Committed to developing impactful, human-centered digital solutions" 
        ),
        "experience_list": Experience.objects.all(),
    }
    return render(request, "index.html", context)

# mengirim data ke experience.html
def show_experience(request):
    context = {
        "nameCard": "AlyaTsbt",
        "name": "Alya Tsabita Imani",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_projects(request):
    context = {
        "name": "Alya tsabita Imani",
        "project_list": Project.objects.all().order_by('-created_at'),
    }
    return render(request, "projects.html", context)