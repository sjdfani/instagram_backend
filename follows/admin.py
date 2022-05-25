from django.contrib import admin
from .models import Following


class FollowingAdmin(admin.ModelAdmin):
    list_display = ('account', 'following', 'created_at')
    list_filter = ('account',)


admin.site.register(Following, FollowingAdmin)
