from django.db import models
from django.contrib.auth.models import User
from comments.models import Comment

class CommentLike(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name='comment_likes')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']
        unique_together = ['owner', 'comment']

    def __str__(self):
        return f"{self.comment} liked by {self.owner}"
