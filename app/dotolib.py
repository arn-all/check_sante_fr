import datetime

import requests


def get_doctolib_availabilities(url):
    """Returns the availabilities as a JSON """
    suffix = url.split("?")[0].split('/')[-1]
    jsonID_url = "https://partners.doctolib.fr/booking/{}.json".format(suffix)
    print(jsonID_url)
    avail_template_url = "https://partners.doctolib.fr/availabilities.json?start_date={date}&visit_motive_ids={motive_id}&agenda_ids={agenda_ids}&practice_ids={practice_id}&profileId={profile_id}"
    print(avail_template_url)
    data = requests.get(jsonID_url).json()['data']
    print(data)
    res = []
    for m, _ in enumerate(data['visit_motives']):
        try:
            avail_variables = {"date": datetime.datetime.now().date().isoformat(),
                               "motive_id": data["visit_motives"][m]['id'],
                               "agenda_ids": "-".join(
                                   [str(data['agendas'][i]['id']) for i, _ in enumerate(data['agendas'])]),
                               "practice_id": data['places'][0]['id'].split('-')[1],
                               'profile_id': data['profile']['id']}
        except IndexError:
            res.append({})
        else:
            res.append(requests.get(avail_template_url.format(**avail_variables)).json())
    return res
