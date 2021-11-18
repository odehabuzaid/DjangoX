from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Topic


class TopicTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="Test_user", email="admin@admin.com", password="Pass123121"
        )

        self.topic = Topic.objects.create(
            title="test_topic",
            student=self.user,
            entries="entries..",
        )

    def test_str(self):
        topic = Topic(title="test_topic")
        self.assertEqual(str(topic), topic.title)
    
    def test_topic_list_view(self):
        response = self.client.get(reverse("topic_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test_topic")
        self.assertTemplateUsed(response, "topics/topic_list.html")
    
    def test_topic_details(self):
        response = self.client.get(reverse("topic_details", args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "title")
        self.assertTemplateUsed(response, "topics/topic_detail.html")
    
    def test_topic_create(self):
        response = self.client.get(reverse("topic_create"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "title")
        self.assertTemplateUsed(response, "topics/topic_form.html")
    
    def test_topic_update(self):
        response = self.client.get(reverse("topic_update", args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "title")
        self.assertTemplateUsed(response, "topics/topic_form.html")
    
    def test_topic_delete(self):
        response = self.client.get(reverse("topic_delete", args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "title")
        self.assertTemplateUsed(response, "topics/topic_confirm_delete.html")
