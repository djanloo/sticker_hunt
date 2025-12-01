from django.db import models

class ScribblePointInfo(models.Model):
    token = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.token

class Scribble(models.Model):
    scribble = models.TextField()
    tag = models.CharField(max_length=100, default='Anonymous')
    scribble_point = models.ForeignKey(
        ScribblePointInfo,
        on_delete=models.PROTECT
    )
    created_at = models.DateTimeField(auto_now_add=True)