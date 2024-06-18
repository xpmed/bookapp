from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg


class Category(models.Model):
    category = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return f"{self.category}"


class Book(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    s_description = models.TextField(max_length=500, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    cover = models.ImageField(upload_to='media/images/', blank=True, null=True)
    average_rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)

    # @property
    # def average_rating(self):
    #     reviews = Review.objects.filter(book__id=self.id)
    #     if reviews:
    #         return reviews.aggregate(Avg('raiting'))['raiting__avg']
    #     return None

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField(max_length=200, blank=True, null=True)
    raiting = models.IntegerField(default=0, blank=True, null=True)
