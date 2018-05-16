from django.contrib import admin

from . import models


class TodoAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'status', 'title', 'create_time', 'update_time',
    )


admin.site.register(models.Todo, TodoAdmin)
