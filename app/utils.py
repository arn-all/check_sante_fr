import requests
from bs4 import BeautifulSoup
from django.core.mail import send_mail
from django.template.loader import render_to_string

from check_sante_fr import settings


def get_departement(code):
    if (not isinstance(code, str)) | (len(code) != 5):
        return ''
    try:
        if int(code[:2]) <= 95:
            return code[:2]
        else:
            return code[:3]
    except ValueError:
        return ''


def list_centre():
    urls = []
    soup = BeautifulSoup(requests.get("https://www.sante.fr/cf/centres-vaccination-covid.html").content.decode('utf8'),
                         'html.parser')
    for li in soup.find_all('li'):
        name = url = zipcode = ville = address = tel = ''
        for cl in li.findAll('span'):
            if 'nom' in cl.get('class'):
                name = cl.get_text()
            elif 'addresse' in cl.get('class'):
                address = cl.get_text()
            elif 'ville' in cl.get('class'):
                city = cl.get_text()
            elif 'telephone' in cl.get('class'):
                tel = cl.get_text().split('-')[1].replace(" ", "")
            elif 'codePostal' in cl.get('class'):
                zipcode = cl.get_text()
            elif "siteWeb" in cl.get('class'):
                url = cl.find('a').get('href').split('?')[0]

        if (url != '') & (name != ''):
            urls.append(
                {'name': name, 'url': url, 'zipcode': zipcode, 'departement': get_departement(zipcode), 'city': city,
                 'address': address, 'phone_number': tel})
    return urls


def send_email_alert(user, value, subscriptions_to_alert):
    msg_plain = render_to_string('email_alert.txt', {"subscriptions_to_alert": subscriptions_to_alert})
    send_mail(
        settings.EMAIL_SUBJECT_PREFIX + " - Nouvelle alerte de suivi",
        msg_plain,
        settings.DEFAULT_FROM_EMAIL,
        [value],
    )
