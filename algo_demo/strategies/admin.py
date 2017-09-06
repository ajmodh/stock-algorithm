from django.contrib import admin

from . import models

class RunAdmin(admin.ModelAdmin):
    list_display = ('stock', 'strategy', 'profit', 'average', 'winrate', 'trades', 'default')
    list_filter = ('default', 'strategy', 'stock' )


admin.site.register(models.Industry)
admin.site.register(models.Stock)
admin.site.register(models.Run, RunAdmin)
