from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author_name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title} by {self.author_name}"
