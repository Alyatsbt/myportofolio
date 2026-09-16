from django.forms import ModelForm, TextInput, Textarea, URLInput

from main.models import Project

class ProjectForm(ModelForm):
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
            "subtitle": "Sub-judul / Tech Stack",
            "description": "Deskripsi Proyek",
            "project_url": "URL Proyek",
            "thumbnail": "URL Gambar Proyek",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "subtitle": TextInput(
                attrs={
                    "placeholder": "Misal: Django, Python, HTML, CSS",
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/Alyatsbt/portofolio",
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }