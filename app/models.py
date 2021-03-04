import json

from django.contrib.auth.models import User
from django.db import models

ALERT_METHOD = [
    ('T', "Télégram"),
    ('E', "Email"),
    ('S', "SMS")
]

BOOKING_PLATFORM = [
    ('D', "Doctolib")
]


class Centre(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    url = models.URLField(unique=True)
    department_number = models.IntegerField(default=0)
    zipcode = models.IntegerField(null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    booking_platform = models.CharField(max_length=1, choices=BOOKING_PLATFORM, default='D')
    date_added = models.DateTimeField(null=False, auto_now_add=True)
    last_check = models.DateTimeField(null=False, auto_now_add=True)
    last_availability = models.IntegerField(null=False, default=0)
    last_json = models.TextField()

    @staticmethod
    def json_stringify(json_data):
        return json.dumps(json_data, separators=(',', ':'))

    @property
    def json_parse(self):
        return json.loads(self.last_json)

    def __str__(self):
        return self.name


class Subscription(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    centre = models.ForeignKey(to=Centre, on_delete=models.CASCADE)
    last_alert = models.DateTimeField(null=False, auto_now_add=True)
    number_alert = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user) + " - " + self.centre.name


class Alert_method(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=ALERT_METHOD, default='T')
    value = models.CharField(max_length=255, null=False, blank=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.user) + " - " + self.value
