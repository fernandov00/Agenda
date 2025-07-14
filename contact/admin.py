from django.contrib import admin

from contact import models 

# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'phone', 'email', 'created_date')