from django.db import models


class Centre(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    url = models.URLField()
    last_check = models.DateTimeField(null=True)
    last_availability = models.IntegerField(null=False, default=0)

    def __str__(self):
        return self.name


class Subscriber(models.Model):
    chat_id = models.CharField(max_length=255, null=False, blank=False)
    subscriptions = models.ManyToManyField(to=Centre, related_name='subscriber')
    last_notification = models.DateTimeField(null=True)

    def __str__(self):
        return self.chat_id
