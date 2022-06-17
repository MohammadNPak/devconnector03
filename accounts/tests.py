from django.test import TestCase
from blog.models import Post, Comment
from django.contrib.auth import get_user_model
from django.test.client import Client
User = get_user_model()
# Create your tests here.
class TestViews(TestCase):

    def setUp(self):
        self.testuser1 = User.objects.create_user(username='testuser1',password="123")
        self.testuser2 = User.objects.create_user(username='testuser2',password="321")
        self.post1 = Post.objects.create(
            title='Test Post 1',
            body = 'This is  test post1',
            date = '2020-01-01',
            author = self.testuser1)
        
        self.post1.likes.set(User.objects.filter(username='testuser1'))
        self.post1.dislikes.set(User.objects.filter(username='testuser2'))
        self.test_client = Client()
        self.test_client.login(username="testuser1", password='123')



    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/index.html')

    def test_posts(self):
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/posts.html')

    def test_post(self):
        response = self.client.get('/posts/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post.html')

    def test_profile(self):
        response = self.client.get('/profile/testuser1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/profile.html')

    def test_dashboard(self):
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/dashboard.html')

    def test_create_profile(self):
        response = self.client.get('/create-profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/create-profile.html')

    def test_register(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')

    def test_login(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    # def test_logout(self):
    #     response = self.client.get('/logout/')
    #     self.