from django.contrib import admin
from .models import Book, Review, Category, Author


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
    list_display = [
        'book_title',
        'raiting',
        'author',
    ]

    def book_title(self, obj):
        return obj.book.title

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'category',
    ]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
