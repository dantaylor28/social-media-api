from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
