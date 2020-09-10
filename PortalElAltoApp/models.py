from django.db import models

# Create your models here.

class Snippet(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    font_size = models.IntegerField()

    def __str__(self):
        return self.title

    def body_preview(self):
        return self.body[:500000]

class PageView(models.Model):
    hits = models.IntegerField(default=0)