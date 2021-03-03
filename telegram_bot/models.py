from django.db import models


class Centre(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    url = models.URLField()
    reservation_url = models.URLField()
    last_check = models.DateTimeField(null=True, auto_now_add=True)
    last_availability = models.IntegerField(null=False, default=0)

    def __str__(self):
        return self.name


class Subscriber(models.Model):
    chat_id = models.CharField(max_length=255, null=False, blank=False)
    subscriptions = models.ForeignKey(to=Centre, related_name='subscriber', on_delete=models.CASCADE, )
    last_notification = models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        return self.chat_id
