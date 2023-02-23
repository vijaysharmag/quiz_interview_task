from django.contrib import admin

from .models import Employee


# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'middle_name',
        'last_name',
        'email',
        'phone_number',
        'working',
    )
    list_filter = ('created', 'modified', 'working')


