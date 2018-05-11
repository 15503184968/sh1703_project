from django.contrib import admin

from . import models


class CardInfoInline(admin.TabularInline):
    model = models.CardInfo


class CardAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'status',
        'balance',
        'balance_available',
        'balance_freeze',
    )
    inlines = [CardInfoInline]


class CardHistoryAdmin(admin.ModelAdmin):
    list_display = (
            'id',
            'time',
            'card',
            'operator_type',
            )


admin.site.register(models.CardStatus)
admin.site.register(models.CardOperateType)
admin.site.register(models.Card, CardAdmin)
admin.site.register(models.CardInfo)
admin.site.register(models.CardHistory)
# admin.site.register(models.CardHistory, CardHistoryAdmin)
