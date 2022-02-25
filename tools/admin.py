from django.contrib import admin
from .models import Team, Tool


# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class ToolAdmin(admin.ModelAdmin):
    exclude = ('date_created', )
    list_display = ('name', 'serial_number')


admin.site.register(Team, TeamAdmin)
admin.site.register(Tool, ToolAdmin)
