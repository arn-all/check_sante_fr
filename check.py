import requests
import datetime
import telegram_send

today = datetime.datetime.now().date().isoformat()
urls = {'Montélimar':"https://partners.doctolib.fr/availabilities.json?start_date={}&visit_motive_ids=2548024&agenda_ids=425174-410507&insurance_sector=public&practice_ids=164545&destroy_temporary=true&limit=7&allowNewPatients=true&telehealth=false&profileId=242583&isOrganization=true&telehealthFeatureEnabled=false&vaccinationMotive=true&vaccinationDaysRange=26&vaccinationCenter=true&nbConfirmedVaccinationAppointments=3316",
        'Valence':"https://partners.doctolib.fr/availabilities.json?start_date={}&visit_motive_ids=2547500&agenda_ids=410324-410327&insurance_sector=public&practice_ids=164487&destroy_temporary=true&limit=7&allowNewPatients=true&telehealth=false&profileId=242529&isOrganization=true&telehealthFeatureEnabled=false&vaccinationMotive=true&vaccinationDaysRange=26&vaccinationCenter=true&nbConfirmedVaccinationAppointments=4881"
        }

for place, url in urls.items():
    data = requests.get(url=url.format(today)).json()

    if (len(data["availabilities"])!=0) | (int(data["total"])!=0):
        telegram_send.send(messages=["Créneau(x) disponible(s) à {}".format(place)])
    else:
        telegram_send.send(messages=["Pas de créneaux à {}".format(place)])
