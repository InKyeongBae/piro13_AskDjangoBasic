from django.db import models
from django.conf import settings
from myproject.utils import uuid_upload_to
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blog_url = models.URLField(blank=True)

class Post(models.Model):
    author_name=models.CharField(max_length=20,null=True,blank=True)
    photo = models.ImageField(upload_to=uuid_upload_to)
    content = models.TextField()
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(allow_unicode=True, db_index=True)
    desc = models.TextField(blank=True)
    comment_count = models.PositiveIntegerField(default=0)
    tag_set = models.ManyToManyField('Tag', blank=True)
    is_publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tag(models.Model): name = models.CharField(max_length=50, unique=True)