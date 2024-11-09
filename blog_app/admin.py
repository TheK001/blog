from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "create_date")
    list_display_links = ("id", "title")
    search_fields = ("title",)