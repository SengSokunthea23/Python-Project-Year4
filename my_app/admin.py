# admin.py
from django.contrib import admin
from .models import Staff, Position

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ['id', 'position_name']
    search_fields = ['position_name']
    ordering = ['position_name']

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['id', 'last_name', 'first_name', 'gender', 'date_of_birth', 'position']
    list_filter = ['gender', 'position', 'date_of_birth']
    search_fields = ['last_name', 'first_name']
    ordering = ['last_name', 'first_name']
    list_select_related = ['position']  # Optimize queries
    
    # Group fields in the admin form
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'gender', 'date_of_birth')
        }),
        ('Job Information', {
            'fields': ('position',)
        }),
    )