from django.shortcuts import render, redirect

from todos_app.todos.forms import CreateTodoForm, UpdateTodoForm, CreateTodoModelForm
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

def create_todo(request):
    form = CreateTodoModelForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'form': form
    }
    return render(request, 'todo_app/create.html', context)

def show_form(request, form):
    context = {
        'form': form
    }
    return render(request, 'todo_app/edit.html', context)

def update_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.method == 'GET':
        return show_form(request, CreateTodoModelForm(initial=todo.__dict__))
    else:
        form = CreateTodoModelForm(
            request.POST,
            instance=todo,
        )
        if form.is_valid():
            form.save()
            return redirect('index')
        return show_form(request, form)
def delete_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect('/')
