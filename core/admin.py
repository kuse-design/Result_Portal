from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Department, User
# Register your models here.

admin.site.register(Department)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'department_code', 'description', 'created_at')
    list_per_page = 10



@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'is_active', 'is_staff', 'created_at')

