from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from todoapp.forms import TaskForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView


class TaskListView(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'task_key'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task_1'


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'updateUV.html'
    context_object_name = 'tesk'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('cbvdetailview', kwargs={'pk': self.object.id})


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('classbasedviewIndex')


# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task_var = Task(name=name, priority=priority, date=date)
        task_var.save()
    task_obj = Task.objects.all()
    return render(request, 'index.html', {"task_key": task_obj})


def detail(request, task_id):
    obj = Task.objects.get(id=task_id)
    return render(request, 'detail.html', {'task_1': obj})


def delete(request, task_id):
    task_obj = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task_obj.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, id):
    task = Task.objects.get(id=id)
    f = TaskForm(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request, 'update.html', {'task': task, 'f': f})
