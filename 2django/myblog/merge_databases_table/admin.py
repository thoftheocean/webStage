from django.contrib import admin
from merge_databases_table.models import ToDo, User

# Register your models here.
admin.site.register(ToDo)
admin.site.register(User)