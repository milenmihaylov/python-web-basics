from django.shortcuts import render, redirect

from todos_app.todos.models import Todo, Person


def index(request):
    # To take all Todos for DB and present them
    context = {
        'todos': Todo.objects.all(),
    }

    return render(request, 'index.html', context)


def create_todo(request):
    text = request.POST['text']
    description = request.POST['description']
    owner_name = request.POST['owner']
    owner = Person.objects\
        .filter(name=owner_name)\
        .first()
    if not owner:
        owner = Person(name=owner_name)
        owner.save()

    todo = Todo(
        text=text,
        description=description,
        owner=owner,
    )
    todo.save()
    return redirect('/')


def change_todo_state(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.state = not todo.state
    todo.save()
    return redirect('/')
