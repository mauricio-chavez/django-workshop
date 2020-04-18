"""TODOs app views"""

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Todo


@login_required
def list(request):
    """TODOs list"""
    finished_todos = Todo.objects.filter(user=request.user, done=True)
    not_finished_todos = Todo.objects.filter(user=request.user, done=False)
    context = {
        'finished_todos': finished_todos,
        'not_finished_todos': not_finished_todos
    }
    return render(request, 'todos/list.html', context)


@login_required
def create(request):
    """Creates a TODO"""
    if request.method == 'POST':
        task = request.POST.get('task')
        todo = Todo.objects.create(task=task, user=request.user)
        messages.success(
            request=request,
            message=f'"{todo.task}" se ha creado correctamente'
        )
        return redirect('todos:list')
    return render(request, 'todos/create.html')


@login_required
def fulfill(request, pk):
    """Fulfills a TODO"""
    todo = get_object_or_404(Todo, pk=pk)
    todo.done = True
    todo.save()
    messages.success(
        request=request,
        message=f'Has completado "{todo.task}"'
    )
    return redirect('todos:list')


@login_required
def delete(request, pk):
    """Deletes a TODO"""
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    messages.success(
        request=request,
        message=f'Se ha eliminado "{todo.task}"'
    )
    return redirect('todos:list')
