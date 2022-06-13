from django.contrib import admin

# Register your models here.
from .models import *

class conceptAdmin(admin.ModelAdmin):
    
    list_display = ('name','concept_type','doctors_name','created_at') 
    search_fields = ('name','concept_type','doctors_name')
    list_filter = ('concept_type','created_at')
admin.site.register(concept,conceptAdmin)
admin.site.register(doctor)
admin.site.register(concept_type)


