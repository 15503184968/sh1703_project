from django.contrib import admin

from . import models


class CardAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'status',
        'balance',
        'balance_available',
        'balance_freeze',
    )


admin.site.register(models.CardStatus)
admin.site.register(models.CardOperateType)
admin.site.register(models.Card, CardAdmin)
admin.site.register(models.CardInfo)
admin.site.register(models.CardHistory)
