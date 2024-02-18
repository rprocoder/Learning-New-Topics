# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class UserAdmin(UserAdmin):
    # You can customize the fields displayed in the admin panel
    list_display = ('username', 'is_staff','bio','birth_date')

# Register your custom user model with the custom admin class
admin.site.register(User, UserAdmin)

