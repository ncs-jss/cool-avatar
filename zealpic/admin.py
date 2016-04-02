from django.contrib import admin
from .models import Zealicon

# Register your models here.
class ZealiconAdmin(admin.ModelAdmin):
    list_display = ['user', 'image']
admin.site.register(Zealicon, ZealiconAdmin)