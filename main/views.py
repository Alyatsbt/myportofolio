from django.shortcuts import render

from main.models import Experience

# mengirim data ke index.html
def show_main(request):
    context = {
        "nameCard": "AlyaTsbt",
        "name": "Alya Tsabita",
        "npm": "2506620192",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "A diligent and dedicated person with a deep interest in digital products design. " 
            "Committed to developing impactful, human-centered digital solutions" 
        ),
    }
    return render(request, "index.html", context)

# mengirim data ke experience.html
def show_experience(request):
    context = {
        "nameCard": "AlyaTsbt",
        "name": "Alya Tsabita",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)