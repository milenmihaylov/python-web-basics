from django.core.exceptions import ValidationError


MAX_TODOS_PER_OWNER = 2


def validate_dot(value):
	if '.' in value:
		raise ValidationError(f'\'.\' is in {value}')


def validate_owner_todos_count(owner):
	if owner.todos_set.count() > MAX_TODOS_PER_OWNER:
		raise ValidationError(f"More than {MAX_TODOS_PER_OWNER}")

