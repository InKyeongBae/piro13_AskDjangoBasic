from django.db import models

# Create your models here.

class Item(models.Model):
    name=models.CharField(max_length=100)
    desc=models.TextField(blank=True)
    price=models.PositiveIntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'<{self.pk}>{self.name}'

    class Meta:
        ordering = ['id']


class Post(models.Model) :
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)