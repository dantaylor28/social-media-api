from django.contrib.auth.models import User
from .models import Like
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class LikeListViewTests(APITestCase):
    def setUp(self):
        dan = User.objects.create_user(username='dan', password='password1')

    def test_list_all_likes(self):
        dan = User.objects.get(username='dan')
        test = Post.objects.create(owner=dan, title='dans post')
        Like.objects.create(owner=dan, post=test)
        response = self.client.get('/likes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_out_cannot_like(self):
        dan = User.objects.get(username='dan')
        post = Post.objects.create(owner=dan, title='dans post')
        response = self.client.post('/likes/', {'post': 'post'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class LikeDetailViewTests(APITestCase):
    def setUp(self):
        dan = User.objects.create_user(username='dan', password='password1')
        sabina = User.objects.create_user(
            username='sabina', password='password1')
        post1 = Post.objects.create(owner=dan, title='dans post')
        post2 = Post.objects.create(owner=sabina, title='sabinas post')
        Like.objects.create(owner=dan, post=post1)
        Like.objects.create(owner=sabina, post=post2)

    def test_get_like_by_id(self):
        response = self.client.get('/likes/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_non_existant_like_id(self):
        response = self.client.get('likes/32')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_own_like(self):
        self.client.login(username='dan', password='password1')
        response = self.client.delete('/likes/1')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_others_like(self):
        self.client.login(username='dan', password='password1')
        response = self.client.delete('/likes/2')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)