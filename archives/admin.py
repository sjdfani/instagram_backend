from django.contrib import admin
from .models import Archive


class ArchiveAdmin(admin.ModelAdmin):
    list_display = ('account', 'post', 'created_at', 'updated_at')
    list_filter = ('account', 'post')
    ordering = ('-created_at',)


admin.site.register(Archive, ArchiveAdmin)
