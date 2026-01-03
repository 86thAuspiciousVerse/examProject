from django.contrib import admin
from .models import Category, Movie, UserCollection, Comment, Share

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'director', 'release_date', 'rating']
    list_filter = ['category', 'release_date']
    search_fields = ['title', 'director', 'actors']
    date_hierarchy = 'release_date'

@admin.register(UserCollection)
class UserCollectionAdmin(admin.ModelAdmin):
    list_display = ['user', 'movie', 'collected_at']
    list_filter = ['collected_at']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'movie', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']

@admin.register(Share)
class ShareAdmin(admin.ModelAdmin):
    list_display = ['user', 'movie', 'created_at']