from django.contrib import admin
from .models import TodoItem, websites
# Register your models here.
admin.site.register(TodoItem)
admin.site.register(websites)