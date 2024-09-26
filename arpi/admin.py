from django.contrib import admin
from .models import Article, Category


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
     list_display = ('title', 'created_at', 'is_active')
     list_display_links = ('title', 'created_at')
     search_fields = ('title', 'category__name')
     list_filter = ('title', 'created_at')
     list_editable = ('is_active',)
     list_per_page = 10



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
     list_display = ('name', 'created_at', 'is_active')
     list_display_links = ('name', 'created_at')
     search_fields = ('name', 'created_at')
     list_filter = ('name', 'created_at')
     list_editable = ('is_active',)
     list_per_page = 10