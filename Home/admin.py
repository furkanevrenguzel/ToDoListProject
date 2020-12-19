from django.contrib import admin

# Register your models here.
from .models import ToDoList, Items


class ToDoListAdmin(admin.ModelAdmin):
    class Meta:
        model = ToDoList


class ItemsAdmin(admin.ModelAdmin):
    class Meta:
        model = Items


admin.site.register(ToDoList, ToDoListAdmin)
admin.site.register(Items, ItemsAdmin)
