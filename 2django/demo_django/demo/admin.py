from django.contrib import admin
from demo.models import *

# Register your models here.

#register方法
# class PublisherAdmin(admin.ModelAdmin):
#     list_display=('name','country','state_province','city')
# admin.site.register(Publisher,PublisherAdmin)

#register装饰器方法
@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display=('name','country','state_province','city')
    search_fields = ('name',)
    ordering = ('city',)
    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('city', 'country'),
        }),
    )


admin.site.register(Author)
admin.site.register(AuthorDetail)

admin.site.register(Book)