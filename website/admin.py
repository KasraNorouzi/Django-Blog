from django.contrib import admin
from .models import Contact
# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('name', 'email', 'created_at')
    list_filter = ('email',)
    search_fields = ('name', 'message', 'email')
