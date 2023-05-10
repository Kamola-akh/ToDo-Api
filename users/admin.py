from django.contrib import admin
from .models import Users


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'email', 'date_of_birth', 'created_at')


admin.site.register(Users, UserAdmin)
