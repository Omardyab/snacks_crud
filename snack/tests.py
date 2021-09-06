from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Snack


class SnackTest(TestCase):
    def setup(self):
        self.user = get_user_model().objects.create_user(
            username="Omardyab", email="Omardyab@email.com", password="1234"
        )
        self.snacks = Snack.objects.create(
            title="nachoos", description="tasty", purchaser=self.user,
        )
    def test_string(self):
        self.assertEqual(str(self.snacks), "nachoos")

    def test_snacks_content(self):
        self.assertEqual(f"{self.snacks.title}", "nachoos")
        self.assertEqual(f"{self.snacks.description}", "tasty")
        self.assertEqual(f"{self.snacks.purchaser}", "Omardyab")

    def test_snack_content(self):
        self.assertEqual(f"{self.snacks.title}", "nachoos")
        self.assertEqual(f"{self.snacks.purchaser}", "Omardyab")
        self.assertEqual(f"{self.snacks.description}", "tasty")

    def test_snack_list_view(self):
        response = self.client.get(reverse("snacks_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "nachoos")
        self.assertTemplateUsed(response, "snack_list.html")

    def test_snack_detail_view(self):
        response = self.client.get(reverse("snack_detail", args="1"))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "purchaser: Omardyab")
        self.assertTemplateUsed(response, "snack_detail.html")

    def test_snack_create_view(self):
        response = self.client.post(
            reverse("snack_create"),
            {
                "title": "alaa",
                "description": "great",
                "purchaser": self.user.id,
            }, follow=True
        )

        self.assertRedirects(response, reverse("snack_detail", args="2"))
        self.assertContains(response, "Details about alaa")

    def test_snack_update_view_redirect(self):
        response = self.client.post(
            reverse("snack_update", args="1"),
            {"title": "Updated name","description":"3","purchaser":self.user.id}
        )

        self.assertRedirects(response, reverse("snack_detail", args="1"))

    def test_snack_delete_view(self):
        response = self.client.get(reverse("snack_delete", args="1"))
        self.assertEqual(response.status_code, 200)
