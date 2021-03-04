from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone

from app.dotolib import get_doctolib_availabilities
from app.models import Centre, Alert_method, Subscription
from app.utils import list_centre, send_email_alert


def update_centre():
    centre_list = list_centre()
    for centre in centre_list:
        if "doctolib" in centre["url"]:
            try:
                new_centre = Centre.objects.get(url=centre["url"])
            except ObjectDoesNotExist:
                new_centre = Centre()
            new_centre.name = centre["name"]
            new_centre.url = centre["url"]
            new_centre.booking_platform = "D"
            new_centre.zipcode = centre["zipcode"]
            new_centre.department_number = centre["departement"]
            new_centre.city = centre["city"]
            new_centre.address = centre["address"]
            new_centre.phone_number = centre["phone_number"]
            new_centre.save()
    # Delete centre that are not in gouvernment website
    Centre.objects.exclude(url__in=[centre["url"] for centre in centre_list]).delete()


def cron_check_availability():
    centre_to_check = Centre.objects.filter(subscription__isnull=False).distinct()
    print(centre_to_check)
    for centre in centre_to_check:
        if centre.booking_platform == "D":
            availabilities = get_doctolib_availabilities(centre.url)
            print(availabilities)


def send_alert():
    user_to_alert = User.objects.filter(subscription__isnull=False).filter(alert_method__isnull=False,
                                                                           alert_method__active=True).filter(
        subscription__last_alert__lt=timezone.now() - timezone.timedelta(hours=4)).filter(
        subscription__centre__last_availability__gt=0).distinct()
    for user in user_to_alert:
        alert_method_list = Alert_method.objects.filter(user=user, active=True)
        subscriptions_to_alert = Subscription.objects.filter(user=user, centre__last_availability__gt=0).distinct()
        for alert_method in alert_method_list:
            if alert_method.type == "M":
                send_email_alert(user, alert_method.value, subscriptions_to_alert)
