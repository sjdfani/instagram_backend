from django.contrib import admin
from .models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'language', 'last_login',
                    'created_at', 'updated_at')
    list_filter = ('language',)
    ordering = ('-created_at',)


admin.site.register(Account, AccountAdmin)
