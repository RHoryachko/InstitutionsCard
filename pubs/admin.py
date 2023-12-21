# establishments/admin.py

from django.contrib import admin
from .models import Establishment, Comment

@admin.register(Establishment)
class EstablishmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'rating', 'category')
    search_fields = ('name', 'address')
    list_filter = ('category',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('establishment', 'author', 'text', 'rating')
    search_fields = ('establishment__name', 'author__username')
    list_filter = ('rating',)
