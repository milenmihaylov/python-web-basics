from django.urls import path

from todos_app.todos.views import index, create_todo, update_todo, delete_todo  # , change_todo_state, show_forms_demo

urlpatterns = [
	path('', index, name='index'),
	path('todos-add/', create_todo, name='create_todo'),
	path('update_todo/<int:pk>', update_todo, name='update_todo'),
	path('delete/<int:pk>', delete_todo),
	# path('change_todo_state/<int:pk>', change_todo_state),
	# path('forms/', show_forms_demo),
]
