from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User, Group
from django.utils import timezone

from main.models import Experience, Project


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
        self.assertEqual(
            response.status_code,
            200
        )
        self.assertTemplateUsed(
            response,
            "experience.html"
        )
        self.assertContains(
            response,
            self.experience.title
        )
        self.assertContains(
            response,
            self.experience.organization
        )

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(
            reverse("main:show_experience")
        )
        self.assertEqual(
            response.status_code,
            200
        )
        self.assertContains(
            response,
            "Belum ada pengalaman yang ditambahkan."
        )

    def test_experience_search_by_title(self):
        Experience.objects.create(
            title="UI UX Designer",
            organization="Compfest",
            description="Mendesain interface.",
        )
        response = self.client.get(
            reverse("main:show_experience"),
            {"title": "UI UX"}
        )
        self.assertEqual(
            response.status_code,
            200
        )
        self.assertContains(
            response,
            "UI UX Designer"
        )
        self.assertNotContains(
            response,
            "Asisten Dosen PBP"
        )

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
        self.assertEqual(
            response.status_code,
            200
        )
        self.assertContains(
            response,
            self.project.title
        )
        self.assertContains(
            response,
            self.project.subtitle
        )
        self.assertContains(
            response,
            self.project.description
        )

    def test_empty_projects_page(self):
        Project.objects.all().delete()
        response = self.client.get(
            reverse("main:show_projects")
        )
        self.assertEqual(
            response.status_code,
            200
        )
        self.assertContains(
            response,
            "Belum ada project yang ditambahkan."
        )

    def test_project_search_by_title(self):
        Project.objects.create(
            title="Portfolio Website",
            subtitle="Personal Portfolio",
            description="A portfolio website.",
        )
        response = self.client.get(
            reverse("main:show_projects"),
            {"title": "Portfolio"}
        )
        self.assertEqual(
            response.status_code,
            200
        )
        self.assertContains(
            response,
            "Portfolio Website"
        )
        self.assertNotContains(
            response,
            "FocusBuddy"
        )


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