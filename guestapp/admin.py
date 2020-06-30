from django.contrib import admin
from .models import Guest

# Register your models here.
class GuestAdmin(admin.ModelAdmin):
    list_display=['name','comment']

admin.site.register(Guest,GuestAdmin)
