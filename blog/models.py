from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


# Create your models here.
class Post(models.Model):
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    #tag
    category = models.ManyToManyField(Category)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return "{} - {}".format(self.title, self.id)





