from django.contrib import admin
from .models import Like


class LikeAdmin(admin.ModelAdmin):
    list_display = ('post', 'account', 'created_at')
    list_filter = ('post', 'account')


admin.site.register(Like, LikeAdmin)
