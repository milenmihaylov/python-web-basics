from django.core.exceptions import ValidationError
from django.test import TestCase

from lost_and_found.objects_posts.models import Object


class ObjectTest(TestCase):
	valid_name = 'MyTestObject',
	valid_image = 'http://image.com',
	valid_width = 500,
	valid_height = 1,
	valid_weight = 1.1,

	@staticmethod
	def create_object(name=valid_name, image=valid_image, width=valid_width, height=valid_height, weight=valid_weight):
		return Object(
			name=name,
			image=image,
			width=width,
			height=height,
			weight=weight,
		)

	def test_whenWidthIs601_expectRaise(self):
		invalid_width = 601
		obj = self.create_object(width=invalid_width)
		with self.assertRaises(ValidationError) as context:
			obj.full_clean()
			obj.save()
		self.assertIsNotNone(context.exception)

