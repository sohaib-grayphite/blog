from django.db import models
from django.contrib.postgres.fields import ArrayField
from django_quill.fields import QuillField
from easy_thumbnails.signals import saved_file
from easy_thumbnails.signal_handlers import generate_aliases

saved_file.connect(generate_aliases)


class Author(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField()
    def __str__(self):
        return self.name


class Blog(models.Model):
    name = models.CharField(max_length=100)
    content = QuillField()
    tags = ArrayField(models.CharField(max_length=100), null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    photo = models.ImageField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

