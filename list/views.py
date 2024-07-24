from django.urls import reverse_lazy
from django.views import generic

from list.form import TaskForm, TagForm
from list.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "list/task_list.html"
    paginate_by = 10


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("list:task-list")


class TaskUpdateView(generic.edit.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("list:task-list")


class TaskDeleteView(generic.edit.DeleteView):
    model = Task
    success_url = reverse_lazy("list:task-list")


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "list/tag_list.html"
    paginate_by = 10


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("list:tag-list")


class TagUpdateView(generic.edit.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("list:tag-list")


class TagDeleteView(generic.edit.DeleteView):
    model = Tag
    success_url = reverse_lazy("list:tag-list")
