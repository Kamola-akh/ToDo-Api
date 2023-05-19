from django.contrib import admin
from .models import Users


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'password', 'last_name', 'email', 'date_of_birth', 'created_at')
    list_filter = ('name', 'created_at', 'date_of_birth')


admin.site.register(Users, UserAdmin)
