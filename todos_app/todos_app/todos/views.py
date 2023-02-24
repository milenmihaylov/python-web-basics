from django.shortcuts import render, redirect

from todos_app.todos.forms import CreateTodoForm, UpdateTodoForm
from todos_app.todos.models import Todo
#
# def show_forms_demo(request):
#     return render(request, 'forms_workshop/forms_demo.html')
#
# def index(request):
#     # To take all Todos for DB and present them
#     context = {
#         'todos': Todo.objects.all(),
#         'form': CreateTodoForm(),
#     }
#
#     return render(request, 'todo_app/../../templates/index.html', context)
#
#
# # noinspection PyUnreachableCode
def create_todo(request):
    # form instance, using request.POST
    form = CreateTodoForm(request.POST)

    if form.is_valid():
        # cleaned_data is available now
        title = form.cleaned_data['title']
        description = form.cleaned_data['description']
        todo = Todo(
            title=title,
            description=description,
            # owner=owner,
        )
        todo.save()
        return redirect('/')

    context = {
        'todos': Todo.objects.all(),
        'form': form
    }

    return render(request, 'todo_app/create.html', context)
#
# def change_todo_state(request, pk):
#     todo = Todo.objects.get(pk=pk)
#     todo.state = not todo.state
#     todo.save()
#     return redirect('/')


def index(request):
    context = {
        'todos': Todo.objects.all()
    }
    return render(request, 'todo_app/index.html', context)

def update_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    form = UpdateTodoForm(request.POST, initial=todo)

    if request.method == 'POST':
        if form.is_valid():
            todo.title = form.cleaned_data['title']
            todo.description = form.cleaned_data['description']
            todo.state = form.cleaned_data['state']
        todo.save()
        return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'todo_app/create.html', context)

def delete_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect('/')
