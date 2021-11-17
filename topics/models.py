from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Topic(models.Model):
    title = models.CharField(max_length=256, help_text="Enter Topic Name")
    student = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    entries = models.TextField()
    
    def get_absolute_url(self):
        return reverse("topic_details", args=[str(self.id)])
    
    def __str__(self):
        return self.title
