# fazeres/views.py
from rest_framework import viewsets
from rest_framework.response import Response  # Adicione esta linha
from .models import ToDo
from .serializers import ToDoSerializer
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ToDoForm

class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

def todo_list(request):
    todos = ToDo.objects.all()
    return render(request, 'fazeres/todo_list.html', {'todos': todos})

def todo_detail(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    return render(request, 'fazeres/todo_detail.html', {'todo': todo})

def todo_create(request):
    if request.method == "POST":
        form = ToDoForm(request.POST)
        if form.is_valid():
            todo = form.save()
            return redirect('todo_detail', pk=todo.pk)
    else:
        form = ToDoForm()
    return render(request, 'fazeres/todo_form.html', {'form': form})

def todo_update(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    if request.method == "POST":
        form = ToDoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save()
            return redirect('todo_detail', pk=todo.pk)
    else:
        form = ToDoForm(instance=todo)
    return render(request, 'fazeres/todo_form.html', {'form': form})

def todo_delete(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    if request.method == "POST":
        todo.delete()
        return redirect('todo_list')
    return render(request, 'fazeres/todo_confirm_delete.html', {'todo': todo})