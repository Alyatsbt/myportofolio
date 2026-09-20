from django.forms import ModelForm, TextInput, Textarea, URLInput, DateInput

from main.models import Project, Experience

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
            "subtitle": "Sub-judul",
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
                    "placeholder": "Misal: web portofolio pribadi berbasis html dan css",
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

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = ["title", "organization", "category", 
                  "thumbnail", "description"]
        
        labels = {
            "title": "Nama Posisi / Peran",
            "organization": "Organisasi / Perusahaan",
            "category": "Kategori",
            "thumbnail": "URL Gambar / Logo",
            "description": "Deskripsi Pekerjaan",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Misal: VPIC of Visual Design", 
                    "maxlength": 255
                }
            ),
            "organization": TextInput(
                attrs={
                    "placeholder": "Misal: COMPFEST 18", 
                    "maxlength": 255
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://link-gambar-kamu.com/logo.png"
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan pencapaian atau tugas utama di peran ini...", 
                    "rows": 4
                }
            )
        }