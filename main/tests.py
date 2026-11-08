from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User, Group
from django.utils import timezone

from main.models import Experience, Project
from rest_framework.test import APITestCase, APIClient


# ============================================================
# EXPERIENCE TEST
# ============================================================

class ExperienceTest(TestCase):

    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            organization="Universitas Indonesia",
            description="Membantu mahasiswa memahami pengembangan web.",
            started_at=timezone.now().date(),
            is_ongoing=True,
        )

    def test_experience_model(self):
        self.assertEqual(
            str(self.experience),
            "Asisten Dosen PBP"
        )
        self.assertEqual(
            self.experience.organization,
            "Universitas Indonesia"
        )
        self.assertTrue(
            self.experience.is_ongoing
        )

    def test_experience_page_is_accessible(self):
        response = self.client.get(
            reverse("main:show_experience")
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        # Data Experience dimuat melalui JavaScript dan API.
        self.assertContains(response, 'id="experience-grid"')
        self.assertContains(response, "/api/experiences/")

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get("/api/experiences/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    def test_experience_search_by_title(self):
        Experience.objects.create(
            title="UI UX Designer",
            organization="Compfest",
            description="Mendesain interface.",
        )
        response = self.client.get(
            "/api/experiences/",
            {"title": "UI UX"}
        )   
        self.assertEqual(response.status_code, 200)
        data = response.json()
        titles = [
            item["fields"]["title"]
            for item in data
        ]
        self.assertIn("UI UX Designer", titles)
        self.assertNotIn("Asisten Dosen PBP", titles)

    def test_completed_experience(self):
        self.experience.is_ongoing = False
        self.experience.ended_at = timezone.now().date()
        self.experience.save()

        self.assertFalse(
            self.experience.is_ongoing
        )
        self.assertIsNotNone(
            self.experience.ended_at
        )


# ============================================================
# PROJECT TEST
# ============================================================

class ProjectTest(TestCase):

    def setUp(self):
        self.project = Project.objects.create(
            title="FocusBuddy",
            subtitle="AI-Powered Task Decomposition",
            description="A cognitive-friendly productivity platform",
            thumbnail="/static/img/focusbuddyframe.png",
            project_url="https://www.figma.com",
        )

    def test_projects_url_is_accessible(self):
        response = self.client.get(
            reverse("main:show_projects")
        )
        self.assertEqual(
            response.status_code,
            200
        )
        self.assertTemplateUsed(
            response,
            "projects.html"
        )

    def test_projects_page_displays_data(self):
        response = self.client.get(
            reverse("main:show_projects")
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "projects.html")

        # Data akan dimuat oleh JavaScript melalui API,
        # jadi kita cukup memastikan elemen grid tersedia.
        self.assertContains(response, 'id="grid"')
        self.assertContains(response, "/api/v1/projects/")

    def test_empty_projects_page(self):
        Project.objects.all().delete()

        response = self.client.get(
            reverse("main:show_projects")
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'id="empty"')

    def test_project_search_by_title(self):
        Project.objects.create(
            title="Portfolio Website",
            subtitle="Personal Portfolio",
            description="A portfolio website.",
        )

        response = self.client.get(
            reverse("api:project-list"),
            {"title": "Portfolio"}
        )

        self.assertEqual(response.status_code, 200)

        projects = response.json()

        self.assertEqual(len(projects), 1)
        self.assertEqual(projects[0]["title"], "Portfolio Website")


# ============================================================
# PERMISSION TEST
# ============================================================

class PermissionTest(TestCase):

    def setUp(self):
        self.superuser = User.objects.create_superuser(
            username="admin",
            password="admin123"
        )
        self.user = User.objects.create_user(
            username="user",
            password="user123"
        )
        self.editor = User.objects.create_user(
            username="editor",
            password="editor123"
        )
        self.editor_group = Group.objects.create(
            name="Editor"
        )
        self.editor.groups.add(
            self.editor_group
        )

        # PROJECT
        self.project = Project.objects.create(
            title="Test Project",
            subtitle="Test Subtitle",
            description="Test Description",
        )

        # EXPERIENCE
        self.experience = Experience.objects.create(
            title="Test Experience",
            organization="Test Organization",
            description="Test Description",
        )

    # ========================================================
    # CREATE PROJECT
    # ========================================================

    def test_superuser_can_access_create_project(self):
        self.client.login(
            username="admin",
            password="admin123"
        )
        response = self.client.get(
            reverse("main:create_project")
        )
        self.assertEqual(
            response.status_code,
            200
        )

    def test_normal_user_cannot_create_project(self):
        self.client.login(
            username="user",
            password="user123"
        )
        response = self.client.get(
            reverse("main:create_project")
        )
        self.assertEqual(
            response.status_code,
            403
        )

    def test_anonymous_user_redirected_from_create_project(self):
        response = self.client.get(
            reverse("main:create_project")
        )
        self.assertEqual(
            response.status_code,
            302
        )
        self.assertTrue(
            response.url.startswith("/login/")
        )

    # ========================================================
    # UPDATE PROJECT
    # ========================================================

    def test_superuser_can_update_project(self):
        self.client.login(
            username="admin",
            password="admin123"
        )
        response = self.client.get(
            reverse(
                "main:update_project",
                args=[self.project.id]
            )
        )
        self.assertEqual(
            response.status_code,
            200
        )

    def test_editor_can_update_project(self):
        self.client.login(
            username="editor",
            password="editor123"
        )
        response = self.client.get(
            reverse(
                "main:update_project",
                args=[self.project.id]
            )
        )
        self.assertEqual(
            response.status_code,
            200
        )

    def test_normal_user_cannot_update_project(self):
        self.client.login(
            username="user",
            password="user123"
        )
        response = self.client.get(
            reverse(
                "main:update_project",
                args=[self.project.id]
            )
        )
        self.assertEqual(
            response.status_code,
            403
        )

    def test_anonymous_user_redirected_from_update_project(self):
        response = self.client.get(
            reverse(
                "main:update_project",
                args=[self.project.id]
            )
        )
        self.assertEqual(
            response.status_code,
            302
        )
        self.assertTrue(
            response.url.startswith("/login/")
        )

    # ========================================================
    # DELETE PROJECT
    # ========================================================

    def test_superuser_can_delete_project(self):
        self.client.login(
            username="admin",
            password="admin123"
        )
        response = self.client.post(
            reverse(
                "main:delete_project",
                args=[self.project.id]
            )
        )
        self.assertEqual(
            response.status_code,
            302
        )
        self.assertFalse(
            Project.objects.filter(
                id=self.project.id
            ).exists()
        )

    def test_editor_cannot_delete_project(self):
        self.client.login(
            username="editor",
            password="editor123"
        )
        response = self.client.post(
            reverse(
                "main:delete_project",
                args=[self.project.id]
            )
        )
        self.assertEqual(
            response.status_code,
            403
        )
        self.assertTrue(
            Project.objects.filter(
                id=self.project.id
            ).exists()
        )

    def test_normal_user_cannot_delete_project(self):
        self.client.login(
            username="user",
            password="user123"
        )
        response = self.client.post(
            reverse(
                "main:delete_project",
                args=[self.project.id]
            )
        )
        self.assertEqual(
            response.status_code,
            403
        )

    # ========================================================
    # CREATE EXPERIENCE
    # ========================================================

    def test_superuser_can_access_create_experience(self):
        self.client.login(
            username="admin",
            password="admin123"
        )
        response = self.client.get(
            reverse("main:create_experience")
        )
        self.assertEqual(
            response.status_code,
            200
        )

    def test_editor_cannot_create_experience(self):
        self.client.login(
            username="editor",
            password="editor123"
        )
        response = self.client.get(
            reverse("main:create_experience")
        )
        self.assertEqual(
            response.status_code,
            403
        )

    def test_normal_user_cannot_create_experience(self):
        self.client.login(
            username="user",
            password="user123"
        )
        response = self.client.get(
            reverse("main:create_experience")
        )
        self.assertEqual(
            response.status_code,
            403
        )

    def test_anonymous_user_redirected_from_create_experience(self):
        response = self.client.get(
            reverse("main:create_experience")
        )
        self.assertEqual(
            response.status_code,
            302
        )
        self.assertTrue(
            response.url.startswith("/login/")
        )

    # ========================================================
    # UPDATE EXPERIENCE
    # ========================================================

    def test_superuser_can_update_experience(self):
        self.client.login(
            username="admin",
            password="admin123"
        )
        response = self.client.get(
            reverse(
                "main:update_experience",
                args=[self.experience.id]
            )
        )
        self.assertEqual(
            response.status_code,
            200
        )

    def test_editor_can_update_experience(self):
        self.client.login(
            username="editor",
            password="editor123"
        )
        response = self.client.get(
            reverse(
                "main:update_experience",
                args=[self.experience.id]
            )
        )
        self.assertEqual(
            response.status_code,
            200
        )

    def test_normal_user_cannot_update_experience(self):
        self.client.login(
            username="user",
            password="user123"
        )
        response = self.client.get(
            reverse(
                "main:update_experience",
                args=[self.experience.id]
            )
        )
        self.assertEqual(
            response.status_code,
            403
        )

    def test_anonymous_user_redirected_from_update_experience(self):
        response = self.client.get(
            reverse(
                "main:update_experience",
                args=[self.experience.id]
            )
        )
        self.assertEqual(
            response.status_code,
            302
        )
        self.assertTrue(
            response.url.startswith("/login/")
        )

    # ========================================================
    # DELETE EXPERIENCE
    # ========================================================

    def test_superuser_can_delete_experience(self):
        self.client.login(
            username="admin",
            password="admin123"
        )
        response = self.client.post(
            reverse(
                "main:delete_experience",
                args=[self.experience.id]
            )
        )
        self.assertEqual(
            response.status_code,
            302
        )
        self.assertFalse(
            Experience.objects.filter(
                id=self.experience.id
            ).exists()
        )

    def test_editor_cannot_delete_experience(self):
        self.client.login(
            username="editor",
            password="editor123"
        )
        response = self.client.post(
            reverse(
                "main:delete_experience",
                args=[self.experience.id]
            )
        )
        self.assertEqual(
            response.status_code,
            403
        )
        self.assertTrue(
            Experience.objects.filter(
                id=self.experience.id
            ).exists()
        )

    def test_normal_user_cannot_delete_experience(self):
        self.client.login(
            username="user",
            password="user123"
        )
        response = self.client.post(
            reverse(
                "main:delete_experience",
                args=[self.experience.id]
            )
        )
        self.assertEqual(
            response.status_code,
            403
        )

    # ========================================================
    # EDITOR GROUP
    # ========================================================

    def test_editor_belongs_to_editor_group(self):
        self.assertTrue(
            self.editor.groups.filter(
                name="Editor"
            ).exists()
        )


# ============================================================
# AUTHENTICATION TEST
# ============================================================

class AuthenticationTest(TestCase):

    def test_register_page_is_accessible(self):
        response = self.client.get(
            reverse("main:register")
        )
        self.assertEqual(
            response.status_code,
            200
        )
        self.assertTemplateUsed(
            response,
            "register.html"
        )

    def test_user_can_register(self):
        response = self.client.post(
            reverse("main:register"),
            {
                "username": "newuser",
                "password1": "StrongPassword123!",
                "password2": "StrongPassword123!",
            }
        )
        self.assertEqual(
            response.status_code,
            302
        )
        self.assertTrue(
            User.objects.filter(
                username="newuser"
            ).exists()
        )

    def test_login_page_is_accessible(self):
        response = self.client.get(
            reverse("main:login")
        )
        self.assertEqual(
            response.status_code,
            200
        )
        self.assertTemplateUsed(
            response,
            "login.html"
        )

    def test_user_can_login(self):
        User.objects.create_user(
            username="testuser",
            password="testpassword123"
        )
        response = self.client.post(
            reverse("main:login"),
            {
                "username": "testuser",
                "password": "testpassword123",
            }
        )
        self.assertEqual(
            response.status_code,
            302
        )
        self.assertEqual(
            response.url,
            reverse("main:show_main")
        )

    def test_user_can_logout(self):
        User.objects.create_user(
            username="testuser",
            password="testpassword123"
        )
        self.client.login(
            username="testuser",
            password="testpassword123"
        )
        response = self.client.get(
            reverse("main:logout")
        )
        self.assertEqual(
            response.status_code,
            302
        )
        self.assertEqual(
            response.url,
            reverse("main:show_main")
        )


# ============================================================
# STAR TEST
# ============================================================

class StarTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="staruser",
            password="starpassword123"
        )
        self.project = Project.objects.create(
            title="Star Project",
            subtitle="Test Project",
            description="Project for star testing",
        )

    def test_authenticated_user_can_star_project(self):
        self.client.login(
            username="staruser",
            password="starpassword123"
        )
        response = self.client.post(
            reverse(
                "main:toggle_star",
                args=[self.project.id]
            )
        )
        self.assertEqual(
            response.status_code,
            302
        )
        self.assertTrue(
            self.project.starred_by.filter(
                id=self.user.id
            ).exists()
        )

    def test_user_can_unstar_project(self):
        self.client.login(
            username="staruser",
            password="starpassword123"
        )
        self.project.starred_by.add(
            self.user
        )
        response = self.client.post(
            reverse(
                "main:toggle_star",
                args=[self.project.id]
            )
        )
        self.assertEqual(
            response.status_code,
            302
        )
        self.assertFalse(
            self.project.starred_by.filter(
                id=self.user.id
            ).exists()
        )

    def test_guest_cannot_star_project(self):
        response = self.client.post(
            reverse(
                "main:toggle_star",
                args=[self.project.id]
            )
        )
        self.assertEqual(
            response.status_code,
            302
        )
        self.assertTrue(
            response.url.startswith("/login/")
        )
        self.assertFalse(
            self.project.starred_by.exists()
        )


# ============================================================
# PROJECT API TEST
# ============================================================

class ProjectAPITest(TestCase):

    def setUp(self):
        self.superuser = User.objects.create_superuser(
            username="admin",
            password="admin123"
        )

        self.user = User.objects.create_user(
            username="user",
            password="user123"
        )

        self.editor = User.objects.create_user(
            username="editor",
            password="editor123"
        )

        self.editor_group = Group.objects.create(
            name="Editor"
        )
        self.editor.groups.add(self.editor_group)

        self.project = Project.objects.create(
            title="FocusBuddy",
            subtitle="AI-Powered Task Decomposition",
            description="A cognitive-friendly productivity platform",
            thumbnail="/static/img/focusbuddyframe.png",
            project_url="https://www.figma.com",
        )

        self.list_url = reverse("api:project-list")
        self.detail_url = reverse(
            "api:project-detail",
            args=[self.project.id]
        )

    def test_editor_can_update_project_through_api(self):
        self.client.force_login(self.editor)

        response = self.client.patch(
            self.detail_url,
            {"title": "Updated by Editor"},
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)

        self.project.refresh_from_db()

        self.assertEqual(
            self.project.title,
            "Updated by Editor"
        )

    def test_editor_cannot_create_project_through_api(self):
        self.client.force_login(self.editor)

        payload = {
            "title": "Editor Project",
            "subtitle": "Test",
            "description": "Should not be created",
        }

        response = self.client.post(
            self.list_url,
            payload,
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 403)

        self.assertFalse(
            Project.objects.filter(
                title="Editor Project"
            ).exists()
        )

    def test_editor_cannot_delete_project_through_api(self):
        self.client.force_login(self.editor)

        response = self.client.delete(self.detail_url)

        self.assertEqual(response.status_code, 403)

        self.assertTrue(
            Project.objects.filter(
                id=self.project.id
            ).exists()
        )

    # --------------------------------------------------------
    # GET PROJECT LIST
    # --------------------------------------------------------

    def test_api_can_get_all_projects(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["title"], "FocusBuddy")

    def test_api_can_search_project_by_title(self):
        Project.objects.create(
            title="Portfolio Website",
            subtitle="Personal Portfolio",
            description="A portfolio website."
        )

        response = self.client.get(
            self.list_url,
            {"title": "Portfolio"}
        )

        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["title"], "Portfolio Website")

    def test_api_returns_empty_list_when_no_project_matches(self):
        response = self.client.get(
            self.list_url,
            {"title": "Nonexistent"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    # --------------------------------------------------------
    # GET PROJECT DETAIL
    # --------------------------------------------------------

    def test_api_can_get_project_detail(self):
        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertEqual(data["id"], str(self.project.id))
        self.assertEqual(data["title"], "FocusBuddy")

    # --------------------------------------------------------
    # POST PROJECT
    # --------------------------------------------------------

    def test_superuser_can_create_project_through_api(self):
        self.client.force_login(self.superuser)

        payload = {
            "title": "New Project",
            "subtitle": "A new project",
            "description": "Created through the API",
            "thumbnail": "",
            "project_url": "",
        }

        response = self.client.post(
            self.list_url,
            payload,
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 201)

        self.assertTrue(
            Project.objects.filter(
                title="New Project"
            ).exists()
        )

    def test_normal_user_cannot_create_project_through_api(self):
        self.client.force_login(self.user)

        payload = {
            "title": "Unauthorized Project",
            "subtitle": "Test",
            "description": "Should not be created",
        }

        response = self.client.post(
            self.list_url,
            payload,
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 403)

        self.assertFalse(
            Project.objects.filter(
                title="Unauthorized Project"
            ).exists()
        )

    def test_anonymous_user_cannot_create_project_through_api(self):
        payload = {
            "title": "Unauthorized Project",
            "subtitle": "Test",
            "description": "Should not be created",
        }

        response = self.client.post(
            self.list_url,
            payload,
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 403)

    # --------------------------------------------------------
    # PATCH PROJECT
    # --------------------------------------------------------

    def test_superuser_can_update_project_through_api(self):
        self.client.force_login(self.superuser)

        response = self.client.patch(
            self.detail_url,
            {
                "title": "Updated FocusBuddy"
            },
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)

        self.project.refresh_from_db()

        self.assertEqual(
            self.project.title,
            "Updated FocusBuddy"
        )

    # --------------------------------------------------------
    # DELETE PROJECT
    # --------------------------------------------------------

    def test_superuser_can_delete_project_through_api(self):
        self.client.force_login(self.superuser)

        response = self.client.delete(self.detail_url)

        self.assertEqual(response.status_code, 204)

        self.assertFalse(
            Project.objects.filter(
                id=self.project.id
            ).exists()
        )



# ============================================================
# EXPERIENCE API TEST
# ============================================================

class ExperienceAPITest(APITestCase):

    def setUp(self):
        # Membuat tiga jenis user
        self.owner = User.objects.create_superuser(
            username="owner",
            email="owner@example.com",
            password="password123"
        )

        self.normal_user = User.objects.create_user(
            username="normal",
            password="password123"
        )

        self.editor = User.objects.create_user(
            username="editor",
            password="password123"
        )

        # Memasukkan editor ke grup Editor
        self.editor_group = Group.objects.create(name="Editor")
        self.editor.groups.add(self.editor_group)

        # Membuat data Experience untuk pengujian
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            organization="Universitas Indonesia",
            description="Membantu mahasiswa memahami pengembangan web.",
            started_at=timezone.now().date(),
            is_ongoing=True,
        )

        # URL API
        self.list_url = reverse("api:experience-list")
        self.detail_url = reverse(
            "api:experience-detail",
            kwargs={"experience_id": self.experience.pk}
        )
        self.star_url = reverse(
            "api:experience-star",
            kwargs={"experience_id": self.experience.pk}
        )

        # Data valid untuk membuat Experience baru
        self.valid_payload = {
            "title": "UI/UX Designer",
            "organization": "BEM Fasilkom UI",
            "description": "Merancang antarmuka aplikasi.",
            "started_at": timezone.now().date().isoformat(),
            "is_ongoing": True,
        }

    # ========================================================
    # PUBLIC ACCESS
    # ========================================================

    def test_anonymous_can_read_experience(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)

    def test_anonymous_cannot_create_experience(self):
        response = self.client.post(
            self.list_url,
            self.valid_payload,
            format="json"
        )

        self.assertEqual(response.status_code, 403)
        self.assertEqual(Experience.objects.count(), 1)

    # ========================================================
    # NORMAL USER
    # ========================================================

    def test_normal_user_can_star_and_unstar(self):
        self.client.force_authenticate(user=self.normal_user)

        # Star Experience
        response = self.client.post(self.star_url)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            self.experience.starred_by.filter(
                pk=self.normal_user.pk
            ).exists()
        )
        self.assertTrue(response.data["is_starred"])

        # Unstar Experience
        response = self.client.post(self.star_url)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(
            self.experience.starred_by.filter(
                pk=self.normal_user.pk
            ).exists()
        )
        self.assertFalse(response.data["is_starred"])

    def test_anonymous_cannot_star(self):
        response = self.client.post(self.star_url)

        self.assertEqual(response.status_code, 403)

    def test_normal_user_cannot_update_or_delete(self):
        self.client.force_authenticate(user=self.normal_user)

        original_title = self.experience.title

        # PATCH harus ditolak
        response = self.client.patch(
            self.detail_url,
            {"title": "Changed Title"},
            format="json"
        )
        self.assertEqual(response.status_code, 403)

        # DELETE harus ditolak
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 403)

        # Pastikan database tidak berubah
        self.experience.refresh_from_db()
        self.assertEqual(self.experience.title, original_title)

    # ========================================================
    # EDITOR
    # ========================================================

    def test_editor_can_update_experience(self):
        self.client.force_authenticate(user=self.editor)

        response = self.client.patch(
            self.detail_url,
            {"title": "Updated Experience"},
            format="json"
        )

        self.assertEqual(response.status_code, 200)

        self.experience.refresh_from_db()
        self.assertEqual(
            self.experience.title,
            "Updated Experience"
        )

    def test_editor_cannot_create_or_delete_experience(self):
        self.client.force_authenticate(user=self.editor)

        # POST harus ditolak
        response = self.client.post(
            self.list_url,
            self.valid_payload,
            format="json"
        )
        self.assertEqual(response.status_code, 403)
        self.assertEqual(Experience.objects.count(), 1)

        # DELETE harus ditolak
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 403)
        self.assertTrue(
            Experience.objects.filter(pk=self.experience.pk).exists()
        )

    # ========================================================
    # PORTFOLIO OWNER
    # ========================================================

    def test_owner_can_create_update_and_delete_experience(self):
        self.client.force_authenticate(user=self.owner)

        # POST: Create
        response = self.client.post(
            self.list_url,
            self.valid_payload,
            format="json"
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Experience.objects.count(), 2)

        new_id = response.data["id"]

        # PUT: Update
        new_detail_url = reverse(
            "api:experience-detail",
            kwargs={"experience_id": new_id}
        )

        updated_payload = {
            **self.valid_payload,
            "title": "Updated by Owner",
        }

        response = self.client.put(
            new_detail_url,
            updated_payload,
            format="json"
        )

        self.assertEqual(response.status_code, 200)

        # DELETE
        response = self.client.delete(new_detail_url)

        self.assertEqual(response.status_code, 204)
        self.assertEqual(Experience.objects.count(), 1)

    # ========================================================
    # VALIDATION & ERROR HANDLING
    # ========================================================

    def test_invalid_title_returns_400(self):
        self.client.force_authenticate(user=self.owner)

        invalid_payload = {
            **self.valid_payload,
            "title": "<b></b>",
        }

        response = self.client.post(
            self.list_url,
            invalid_payload,
            format="json"
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(Experience.objects.count(), 1)

    def test_nonexistent_experience_returns_404(self):
        import uuid

        nonexistent_url = reverse(
            "api:experience-detail",
            kwargs={"experience_id": uuid.uuid4()}
        )

        response = self.client.get(nonexistent_url)

        self.assertEqual(response.status_code, 404)

    # ========================================================
    # CSRF PROTECTION
    # ========================================================

    def test_authenticated_session_request_without_csrf_is_denied(self):
        csrf_client = APIClient(enforce_csrf_checks=True)

        # Login menggunakan session authentication
        logged_in = csrf_client.login(
            username="owner",
            password="password123"
        )
        self.assertTrue(logged_in)

        # POST tanpa CSRF token harus ditolak
        response = csrf_client.post(
            self.list_url,
            self.valid_payload,
            format="json"
        )

        self.assertEqual(response.status_code, 403)
        self.assertEqual(Experience.objects.count(), 1)
