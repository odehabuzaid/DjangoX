from django.urls.base import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .models import Topic


class TopicListView(ListView):
    model = Topic
    template_name = "learning_journal/topic_list.html"
    context_object_name = "topic_list"


class TopicDetailView(DetailView):
    model = Topic
    name = "learning_journal/topic_details.html"
    context_object_name = "topic_details"


class TopicCreateView(CreateView):
    model = Topic
    name = "learning_journal/topic_create.html"
    fields = ["title", "student", "entries"]


class TopicUpdateView(UpdateView):
    model = Topic
    name = "learning_journal/topic_update.html"
    fields = ["title", "student", "entries"]


class TopicDeleteView(DeleteView):
    model = Topic
    name = "learning_journal/topic_delete.html"
    success_url = reverse_lazy("topic_list")
