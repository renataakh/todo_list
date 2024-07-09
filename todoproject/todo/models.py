from django.db import models


# Create your models here.

class TodoList(models.Model):
    text = models.CharField(max_length=50)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['time_create']
