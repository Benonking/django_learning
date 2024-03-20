## -- need a coment here
from django.test import TestCase

# Create your tests here.
# reference active user
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post

class BlogTests(TestCase):
	def setUp(self):
		'''create set up methode '''
		self.user = get_user_model().objects.create_user(
			username='testuser',
			email='test@email.com',
			password='secret'
		)
		self.post = Post.objects.create(
			title='A test Title',
			body='A test bosy',
			author=self.user
		)
	
	def test_string_representaion(self):
		'''check if strig representation of post is correct'''
		post = Post(title='A test Title')
		self.assertEqual(str(post), post.title)
	
	def test_post_content(self):
		self.assertEqual(f"{self.post.title}", 'A test Title')
		self.assertEqual(f"{self.post.author}", 'testuser')
		self.assertEqual(f"{self.post.body}", 'A test body')
	
	def test_post_list_view(self):
		'''check if homepage returns status code 200'''
		response = self.client.get(reverse('home'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'A test body')
		self.assertTemplateUsed(response, 'home.html')
	
	def test_post_detail_view(self):
		'''check if detail view works as expected'''
		response = self.client.get('/post/1')
		no_response = self.client.get('/post/100')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(no_response.status_code, 404)
		self.assertContains(response, 'A test Title')
		self.assertTemplateUsed(response, 'post_detail.html')

