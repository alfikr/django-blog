from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=False)
    body = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    tumb = models.ImageField(default='default.png', blank=True)
    # add author later

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50]+"..."