from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    author = models.CharField(max_length=100)
    year_published = models.IntegerField()
    genres = models.CharField(max_length=100)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title