from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    author = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        if len(self.content.split()) > 2000:
            raise ValidationError('Content should contain max 2000 words.')
        super().save(*args, **kwargs)


