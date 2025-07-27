from django.contrib import admin
from contact import models 

# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'lastname', 'phone', 'email', 'created_date', 'show',
    list_editable = 'show', 
    list_display_links = 'id',
    
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
