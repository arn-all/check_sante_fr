import requests
import datetime
import telegram_send

today = datetime.datetime.now().date().isoformat()
centres = [{'place':'Montélimar',
        'request_url':"https://partners.doctolib.fr/availabilities.json?start_date={}&visit_motive_ids=2548024&agenda_ids=425174-410507&insurance_sector=public&practice_ids=164545&destroy_temporary=true&limit=7&allowNewPatients=true&telehealth=false&profileId=242583&isOrganization=true&telehealthFeatureEnabled=false&vaccinationMotive=true&vaccinationDaysRange=26&vaccinationCenter=true&nbConfirmedVaccinationAppointments=3316",
        'link_url': "https://partners.doctolib.fr/centre-de-sante/montelimar/centre-de-vaccination-covid-gh-portes-de-provence-montelimar?speciality_id=5494&enable_cookies_consent=1"},
        {'place':'Valence',
        'request_url':'https://partners.doctolib.fr/availabilities.json?start_date={}&visit_motive_ids=2547500&agenda_ids=410324-410327&insurance_sector=public&practice_ids=164487&destroy_temporary=true&limit=7&allowNewPatients=true&telehealth=false&profileId=242529&isOrganization=true&telehealthFeatureEnabled=false&vaccinationMotive=true&vaccinationDaysRange=26&vaccinationCenter=true&nbConfirmedVaccinationAppointments=4881',
        'link_url':"https://partners.doctolib.fr/hopital-public/valence/centre-de-vaccination-du-centre-hospitalier-de-valence?speciality_id=5494&enable_cookies_consent=1"}
        ] 

for centre in centres:
    data = requests.get(url=centre['request_url'].format(today)).json()

    if (len(data["availabilities"])!=0) | (int(data["total"])!=0):
        telegram_send.send(messages=["🔔💉 Créneau(x) disponible(s) à {}. Plus d'info: {}".format(centre['place'], centre['link_url'])], 
                            disable_web_page_preview=True)
    # else:
    #     telegram_send.send(messages=["🙅‍♂️💉 Pas de créneaux à {}. Plus d'info: {}".format(centre['place'], centre['link_url'])], 
    #                         disable_web_page_preview=True)
