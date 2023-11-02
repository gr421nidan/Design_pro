from django.contrib import admin
from .models import *
admin.site.register(CustomUser)
admin.site.register(Category)
@admin.register(Application)
class ApplicationsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category', 'date', 'status')
    model = Application
