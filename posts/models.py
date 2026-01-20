from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    """
    The Post model which contains all relevant fields for any posts created.
    A default image is attached in the case of a user not uploading one
    themselves.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    caption = models.TextField(blank=True)
    tags = models.ManyToManyField(
        "tags.Tag",
        related_name="posts",
        blank=True
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post_image = models.ImageField(
        upload_to='images/',
        default='../placeholder_post_pic_x9ygad'
    )

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return f"post title: {self.title} | by: {self.owner}"
    
