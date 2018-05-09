from django.contrib import admin

from . import models


admin.site.register(models.CardStatus)
admin.site.register(models.CardOperateType)
admin.site.register(models.Card)
admin.site.register(models.CardInfo)
admin.site.register(models.CardHistory)
