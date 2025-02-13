from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    caption = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post_image = models.ImageField(
        upload_to='images/', default='../placeholder_post_pic_x9ygad', blank=True
    )

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return f"post title: {self.title} by: {self.owner}"
    
