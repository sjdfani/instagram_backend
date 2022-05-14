from django.contrib import admin
from .models import Post, Tags


class PostAdmin(admin.ModelAdmin):
    list_display = ('account', 'created_at', 'updated_at', 'status')
    list_filter = ('account', 'status')
    ordering = ('-created_at',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_at')
    list_filter = ('post', 'status')
    ordering = ('-created_at',)


admin.site.register(Post, PostAdmin)
admin.site.register(Tags, TagAdmin)
