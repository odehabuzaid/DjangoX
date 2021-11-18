from django.urls.base import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .models import Topic


class TopicListView(ListView):
    model = Topic
    template_name = "topics/topic_list.html"
    context_object_name = "topic_list"


class TopicDetailView(DetailView):
    model = Topic
    name = "topics/topic_detail.html"
    context_object_name = "topic_detail"


class TopicCreateView(CreateView):
    model = Topic
    name = "topics/topic_form.html"
    fields = ["title", "student", "entries"]
    context_object_name = "topic_form"

class TopicUpdateView(UpdateView):
    model = Topic
    name = "topics/topic_update.html"
    fields = ["title", "student", "entries"]


class TopicDeleteView(DeleteView):
    model = Topic
    name = "topics/topic_delete.html"
    success_url = reverse_lazy("topic_list")
