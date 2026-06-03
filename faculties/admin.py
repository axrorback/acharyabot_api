from django.contrib import admin
from .models import Faculty

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('title_uz',)
    prepopulated_fields = {'slug': ('title_en',)}