from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Snack


class SnackTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="Test_user", email="admin@admin.com", password="Pass123121"
        )

        self.snack = Snack.objects.create(
            title="test_snack",
            purchaser=self.user,
            description="test_snack description",
        )

    def test_str(self):
        snack = Snack(title="test_snack")
        self.assertEqual(str(snack), snack.title)

    def test_snack_list_view(self):
        response = self.client.get(reverse("snack_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test_snack")
        self.assertTemplateUsed(response, "snack_list.html")

    def test_snack_details(self):
        response = self.client.get(reverse("snack_details", args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "title")
        self.assertTemplateUsed(response, "snack_details.html")

    def test_snack_create(self):
        response = self.client.get(reverse("snack_create"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "title")
        self.assertTemplateUsed(response, "snack_create.html")

    def test_snack_update(self):
        response = self.client.get(reverse("snack_update", args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "title")
        self.assertTemplateUsed(response, "snack_update.html")

    def test_snack_delete(self):
        response = self.client.get(reverse("snack_delete", args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "title")
        self.assertTemplateUsed(response, "snack_delete.html")
