from django.db import models

class Scribble(models.Model):
    scribble = models.TextField()
    tag = models.CharField(max_length=100, default='Anonymous')
    created_at = models.DateTimeField(auto_now_add=True)

