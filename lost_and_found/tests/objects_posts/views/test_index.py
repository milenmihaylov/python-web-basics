from unittest.mock import patch

from django.test import TestCase, Client
from django.urls import reverse


class IndexViewTest(TestCase):
	@patch('lost_and_found.objects_posts.models.Post.objects')
	def test_example(self, post_mock):
		post_mock.all.return_value = [1]
		client = Client()
		response = client.get(reverse('index'))
		self.assertTemplateUsed(response, 'index.html')


