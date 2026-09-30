from django import forms
from main.models import Project, Experience
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "subtitle",
            "description",
            "project_url",
            "thumbnail",
        ]

        labels = {
            "title": "Nama Proyek",
            "subtitle": "Sub-judul",
            "description": "Deskripsi Proyek",
            "project_url": "URL Proyek",
            "thumbnail": "URL Gambar Proyek",
        }

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "subtitle": forms.TextInput(
                attrs={
                    "placeholder": "Misal: web portofolio pribadi berbasis html dan css",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "project_url": forms.URLInput(
                attrs={
                    "placeholder": "https://github.com/Alyatsbt/portofolio",
                }
            ),
            "thumbnail": forms.URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }
    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Nama proyek tidak boleh hanya berisi tag HTML.")
        return title

    def clean_tech_stack(self):
        return strip_tags(self.cleaned_data["tech_stack"]).strip()

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()



class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ["title", "organization", "thumbnail", "description", "started_at", "ended_at", "is_ongoing"]
        
        labels = {
            "title": "Nama Posisi / Peran",
            "organization": "Organisasi / Perusahaan",
            "thumbnail": "URL Gambar / Logo",
            "description": "Deskripsi Pekerjaan",
            "started_at": "Tanggal Mulai",
            "ended_at": "Tanggal Selesai",
            "is_ongoing": "Sedang Berlangsung?",
        }
        
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "Misal: VPIC of Visual Design", 
                    "maxlength": 255
                }
            ),
            "organization": forms.TextInput(
                attrs={
                    "placeholder": "Misal: COMPFEST 18", 
                    "maxlength": 255
                }
            ),
            "thumbnail": forms.URLInput(
                attrs={
                    "placeholder": "https://link-gambar-kamu.com/logo.png"
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "Ceritakan pencapaian atau tugas utama di peran ini...", 
                    "rows": 4
                }
            ),
            "started_at": forms.DateInput(
                attrs={
                    "type": "date"
                }
            ),
            "ended_at": forms.DateInput(
                attrs={
                    "type": "date"
                }
            ),
        }