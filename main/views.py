from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.models import Experience, Project
from main.forms import ProjectForm, ExperienceForm


# mengirim data ke homepage.html
def show_main(request):
    experiences = Experience.objects.all().order_by('-started_at')
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
    return render(request, "homepage.html", context)

# mengirim data ke experience.html
def show_experience(request):
    experiences = Experience.objects.all().order_by('-started_at')
    context = {
        "nameCard": "AlyaTsbt",
        "name": "Alya Tsabita Imani",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

# ================= FUNGSI BARU TUTORIAL 3 =================

def show_projects(request):
    json_response = get_projects_json(request)
    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Alya Tsabita Imani",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "projects.html", context)

def create_project(request):
    # Menginisialisasi form dengan data POST jika ada, atau form kosong jika tidak ada
    form = ProjectForm(request.POST or None)

    # Mengecek apakah request adalah POST dan data form valid
    if request.method == "POST" and form.is_valid():
        form.save() # Simpan ke database
        messages.success(request, "Proyek baru berhasil ditambahkan!") # Kirim notif
        return redirect("main:show_projects") # Lempar balik ke halaman projects

    context = {
        "name": "Alya Tsabita Imani",
        "form": form,
    }
    return render(request, "projects_form.html", context)

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")

# ================= FUNGSI BARU TUGAS 3 =================

def update_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    form = ProjectForm(request.POST or None, instance=project)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("main:show_projects")
    context = {'form': form}
    return render(request, "projects_form.html", context)

def create_experience(request):
    form = ExperienceForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("main:show_experience")
    return render(request, "experience_form.html", {"form": form})

def update_experience(request, id):
    # Ambil data experience yang mau diedit berdasarkan ID
    experience = get_object_or_404(Experience, pk=id)
    # Masukkan data lama ke dalam form
    form = ExperienceForm(request.POST or None, instance=experience)
    
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("main:show_experience")
    return render(request, "experience_form.html", {"form": form})

def delete_experience(request, id):
    experience = get_object_or_404(Experience, pk=id)
    if request.method == "POST":
        experience.delete()
    return redirect("main:show_experience")

def get_experiences_json(request):
    experiences = Experience.objects.all()
    return HttpResponse(serializers.serialize("json", experiences), content_type="application/json")