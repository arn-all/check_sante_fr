import time

import requests
from django.core.mail import mail_admins
from django.template.loader import render_to_string
from django.utils import timezone

from telegram_bot.models import Centre, Subscriber


def check_centre(centre):
    max_attempts = 3
    attempt = 0
    while attempt < max_attempts:
        try:
            response = requests.get(url=centre.url.format(timezone.now().date().isoformat()))
            data = response.json()
            centre.last_check = timezone.now()
            centre.last_availability = data["total"]
            centre.save()
        except:
            attempt += 1
            time.sleep(60)
        else:
            break
    if attempt == max_attempts:
        msg_plain = render_to_string('email_bug.txt',
                                     {'centre': centre, 'heure': timezone.now()})
        mail_admins("Problème récupération flux " + centre.name, msg_plain)
        print("ERROR")


def alert_subscriber(subscriber):
    print(subscriber)


def cron_check_availability():
    centre_to_check = Centre.objects.filter(subscriber__isnull=False).distinct()
    print(centre_to_check)
    for centre in centre_to_check:
        check_centre(centre)
    subscriber_to_alert = Subscriber.objects.filter(
        last_notification__lt=timezone.now() - timezone.timedelta(hours=4)).filter(
        subscriptions__last_availability__gt=0).distinct()
    print(subscriber_to_alert)
    for subscriber in subscriber_to_alert:
        alert_subscriber(subscriber)
