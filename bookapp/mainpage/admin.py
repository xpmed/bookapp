from django.contrib import admin
from .models import Book, Review, Category


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'author',
        'description',
        'category',
    ]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'category',
    ]


