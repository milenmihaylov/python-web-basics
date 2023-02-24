from django.shortcuts import render, redirect

from todos_app.forms_workshop.forms import WorkshopForm
from todos_app.forms_workshop.models import User


def fill_out_the_form(request):
	if request.method == 'POST':
		form = WorkshopForm(request.POST)

		if form.is_valid():
			name = form.cleaned_data['name']
			age = form.cleaned_data['age']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			text = form.cleaned_data['text']

			user = User(
				name=name,
				age=age,
				email=email,
				password=password,
				text=text,
			)
			user.save()

			print(f"""VALIDATION SUCCESS
	NAME: {name}
	AGE: {age}
	EMAIL: {email}
	PASSWORD: {password}
	TEXT: {text}""")

			return redirect('/workshop/')
		context = {
			'form': form,
		}
		return render(request, 'forms_workshop/workshop_index.html', context)

	else:
		context = {
			'form': WorkshopForm(),
		}
		return render(request, 'forms_workshop/workshop_index.html', context)
