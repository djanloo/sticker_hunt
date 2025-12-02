from django.db import models

class ScribblePointInfo(models.Model):
    token = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=30)
    image_name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.token

    @property
    def image_url(self):
        if self.image_name:
            return f'{self.image_name}'
        return 'default.png'

class Scribble(models.Model):
    scribble = models.TextField()
    tag = models.CharField(max_length=100, default='Anonymous')
    scribble_point = models.ForeignKey(
        ScribblePointInfo,
        on_delete=models.PROTECT
    )
    created_at = models.DateTimeField(auto_now_add=True)