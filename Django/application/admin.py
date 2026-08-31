from django.contrib import admin
from .models import Note
# Register your models here.
class NoteAdmin(admin.ModelAdmin):
    list_display = ('Title', 'isPublish', 'Created_AT')
admin.site.register(Note)