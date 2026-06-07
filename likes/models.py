from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

class Like(models.Model):
    """
    The Like model which has 2 foreign keys relating to User and
    Post. Contains information of the user who Liked the post and
    the post which they Liked.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='likes'
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f"{self.owner} | liked: {self.post}"
