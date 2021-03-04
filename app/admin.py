from django.contrib import admin

from app.models import Centre, Subscription, Alert_method


# Register your models here.


@admin.register(Centre, Subscription, Alert_method)
class StandardAdmin(admin.ModelAdmin):
    pass
