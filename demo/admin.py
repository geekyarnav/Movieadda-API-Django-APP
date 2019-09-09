from django.contrib import admin
from .models import Book,BookNumber
# Register your models here.
# GENERAL APPROACH WE CANT DO MODIFICATION
# admin.site.register(Book)
# WE CAN DO MODIFICATION IN ADMIN BY MAKING IT DECORATORS 'PYTHON'
@admin.register(Book)

class BookAdmin(admin.ModelAdmin):
    # fields =['title','description']
    list_display=['title','description']
    list_filter=['is_published']
    search_fields=['title','description']

admin.site.register(BookNumber)    