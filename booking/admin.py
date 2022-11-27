from django.contrib import admin
from .models import Workshop


class WorkshopAdmin(admin.ModelAdmin):
    list_filter = ('day', 'time',)
    list_display = ('day', 'time',)


admin.site.register(Workshop, WorkshopAdmin)
