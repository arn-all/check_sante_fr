from django.contrib import admin

from telegram_bot.models import Centre, Subscriber


# Register your models here.


@admin.register(Centre, Subscriber)
class StandardAdmin(admin.ModelAdmin):
    pass
