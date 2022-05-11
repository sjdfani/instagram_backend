from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('account', 'created_at', 'updated_at', 'status')
    list_filter = ('account', 'status')
    ordering = ('-created_at',)
