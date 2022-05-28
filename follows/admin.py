from django.contrib import admin
from .models import Follower, Following


class FollowingAdmin(admin.ModelAdmin):
    list_display = ('account', 'following', 'created_at')
    list_filter = ('account',)


class FollowerAdmin(admin.ModelAdmin):
    list_display = ('account', 'follower', 'created_at')
    list_filter = ('account',)


admin.site.register(Following, FollowingAdmin)
admin.site.register(Follower, FollowerAdmin)
