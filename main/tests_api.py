
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from main.models import Project


User = get_user_model()


class ProjectAPITest(TestCase):

    def setUp(self):
        # Membuat API client untuk mengirim HTTP request
        self.client = APIClient()

        # Membuat superuser (pemilik portfolio)
        self.admin = User.objects.create_superuser(
            username="admin_test",
            password="testpassword123"
        )

        # Membuat user biasa
        self.user = User.objects.create_user(
            username="user_test",
            password="testpassword123"
        )

        # Membuat satu project untuk kebutuhan testing
        self.project = Project.objects.create(
            title="Test Project",
            subtitle="Project untuk API testing",
            description="Ini adalah project percobaan."
        )

        # URL endpoints
        self.list_url = reverse("api:project-list")
        self.detail_url = reverse(
            "api:project-detail",
            kwargs={"project_id": self.project.id}
        )
        self.star_url = reverse(
            "api:project-star",
            kwargs={"project_id": self.project.id}
        )

    # ==========================================
    # GET PROJECTS
    # ==========================================

    def test_get_project_list(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Test Project")

    def test_get_project_detail(self):
        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Project")

    # ==========================================
    # CREATE PROJECT
    # ==========================================

    def test_admin_can_create_project(self):
        self.client.force_authenticate(user=self.admin)

        payload = {
            "title": "New Project",
            "subtitle": "Project baru",
            "description": "Project yang dibuat melalui API."
        }

        response = self.client.post(
            self.list_url,
            payload,
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(
            Project.objects.filter(title="New Project").exists()
        )

    def test_regular_user_cannot_create_project(self):
        self.client.force_authenticate(user=self.user)

        payload = {
            "title": "Unauthorized Project",
            "subtitle": "Percobaan user biasa",
            "description": "Tidak seharusnya berhasil."
        }

        response = self.client.post(
            self.list_url,
            payload,
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ==========================================
    # UPDATE PROJECT
    # ==========================================

    def test_admin_can_update_project(self):
        self.client.force_authenticate(user=self.admin)

        payload = {
            "title": "Updated Project"
        }

        response = self.client.patch(
            self.detail_url,
            payload,
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.project.refresh_from_db()
        self.assertEqual(self.project.title, "Updated Project")

    # ==========================================
    # DELETE PROJECT
    # ==========================================

    def test_admin_can_delete_project(self):
        self.client.force_authenticate(user=self.admin)

        response = self.client.delete(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(
            Project.objects.filter(id=self.project.id).exists()
        )

    # ==========================================
    # STAR PROJECT
    # ==========================================

    def test_authenticated_user_can_star_project(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.post(self.star_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(
            self.project.starred_by.filter(pk=self.user.pk).exists()
        )

    def test_star_project_can_be_toggled_off(self):
        self.client.force_authenticate(user=self.user)

        # Star pertama: menambahkan user
        self.client.post(self.star_url)

        # Star kedua: menghapus user
        response = self.client.post(self.star_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(
            self.project.starred_by.filter(pk=self.user.pk).exists()
        )

    def test_anonymous_user_cannot_star_project(self):
        response = self.client.post(self.star_url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
