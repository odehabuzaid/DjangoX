from django.urls import path

from .views import (
    TopicCreateView,
    TopicDeleteView,
    TopicDetailView,
    TopicListView,
    TopicUpdateView,
)

urlpatterns = [
    path("", TopicListView.as_view(), name="topic_list"),
    path("<int:pk>", TopicDetailView.as_view(), name="topic_details"),
    path("create", TopicCreateView.as_view(), name="topic_create"),
    path("<int:pk>/update/", TopicUpdateView.as_view(), name="topic_update"),
    path("<int:pk>/delete/", TopicDeleteView.as_view(), name="topic_delete"),
]
