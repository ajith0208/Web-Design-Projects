from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy

from todoapp.form import TaskForm
from todoapp.models import Task

# Class View
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


class TaskLV(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'tasks'


class TaskDV(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'tasks'


class TaskUV(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'tasks'
    fields = ('task', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('todoapp:cbvdetail', kwargs={'pk': self.object.id})


class TaskDeV(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('todoapp:cbvhome')


# Function view
def home(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(task=name, priority=priority, date=date)
        task.save()
    return render(request, 'index.html', {'tasks': tasks})


def delete(request, taskid):
    task = Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, taskid):
    task = Task.objects.get(id=taskid)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'f': form, 'task': task})
