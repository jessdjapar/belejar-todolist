from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='images/', default=None, blank=True, null=True)

    def __str__(self):
        return self.title
