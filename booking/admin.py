from django.contrib import admin
from .models import Workshop, TIME_SLOTS


class WorkshopAdmin(admin.ModelAdmin):
    list_filter = ('day', 'time',)
    list_display = ('user', 'day', 'time',)


admin.site.register(Workshop, WorkshopAdmin)
