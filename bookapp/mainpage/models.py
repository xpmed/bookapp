from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return f"{self.category}"


class Author(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    surname = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)

    @property
    def full_name(self):
        return f'{self.name} {self.surname}'

    def __str__(self):
        return self.full_name

class Book(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    s_description = models.TextField(max_length=500, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    cover = models.ImageField(upload_to='media/images/', blank=True, null=True)
    average_rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField(max_length=500, blank=True, null=True)
    raiting = models.IntegerField(default=0, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
