from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render
import datetime

from django.contrib.auth.decorators import login_required  
from django.core.exceptions import PermissionDenied        

from main.models import Experience, Project
from main.forms import ProjectForm, ExperienceForm


# mengirim data ke homepage.html
def show_main(request):
    experiences = Experience.objects.all().order_by('-started_at')
    last_login = request.COOKIES.get("last_login", "Belum ada sesi login / Cookie tidak ditemukan")
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
        "last_login": last_login,
    }
    return render(request, "homepage.html", context)

# mengirim data ke experience.html
def show_experience(request):
    experiences = Experience.objects.all().order_by('-started_at')
    query = request.GET.get("title", "").strip()
    if query:
        experiences = experiences.filter(title__icontains=query)
    is_editor = False
    if request.user.is_authenticated:
        is_editor = request.user.groups.filter(name='Editor').exists()
    context = {
        "nameCard": "AlyaTsbt",
        "name": "Alya Tsabita Imani",
        "query": query,
        "experience_list": experiences,
        "is_editor": is_editor,
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

    is_editor = False
    if request.user.is_authenticated:
        is_editor = request.user.groups.filter(name='Editor').exists()

    context = {
        "name": "Alya Tsabita Imani",
        "project_list": projects,
        "title_query": title_query,
        "is_editor": is_editor,
    }
    return render(request, "projects.html", context)


@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
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


@login_required(login_url="/login/")
def delete_project(request, project_id):
    if not request.user.is_superuser:
            raise PermissionDenied
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
    projects_json = serializers.serialize("json", projects, use_natural_foreign_keys=True)
    return HttpResponse(projects_json, content_type="application/json")

# ================= FUNGSI BARU TUGAS 3 =================

@login_required(login_url="/login/")
def update_project(request, project_id):
    is_editor = request.user.groups.filter(name='Editor').exists()
    if not (request.user.is_superuser or is_editor):
        raise PermissionDenied
    
    project = get_object_or_404(Project, pk=project_id)
    form = ProjectForm(request.POST or None, instance=project)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("main:show_projects")
    context = {'form': form}
    return render(request, "projects_form.html", context)


@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    form = ExperienceForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("main:show_experience")
    return render(request, "experience_form.html", {"form": form})


@login_required(login_url="/login/")
def update_experience(request, id):
    is_editor = request.user.groups.filter(name='Editor').exists()
    if not (request.user.is_superuser or is_editor):
        raise PermissionDenied
    
    # Ambil data experience yang mau diedit berdasarkan ID
    experience = get_object_or_404(Experience, pk=id)
    # Masukkan data lama ke dalam form
    form = ExperienceForm(request.POST or None, instance=experience)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("main:show_experience")
    return render(request, "experience_form.html", {"form": form})


@login_required(login_url="/login/")
def delete_experience(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    experience = get_object_or_404(Experience, pk=id)
    if request.method == "POST":
        experience.delete()
    return redirect("main:show_experience")


def get_experiences_json(request):
    experiences = Experience.objects.all()
    return HttpResponse(serializers.serialize("json", experiences), content_type="application/json")

# ================= FUNGSI BARU TUTORIAL 4 =================

def register(request):
    form = UserCreationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")
    context = {
        "name": "Alya Tsabita Imani",
        "form": form,
    }
    return render(request, "register.html", context)


def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response
    context = {
        "name" : "Alya Tsabita Imani",
        "form" : form,
    }
    return render(request, "login.html", context)


def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response


@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_projects")