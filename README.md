# 💉 Surveillance des créneaux de vaccination Covid disponibles

- Requêtes régulières sur doctolib
- Pour déterminer à quelle URL faire la requête: 
  - `Firefox > Menu > Web Developer > Network`, et rechercher un créneau via l'interface du site 
  - Ouvrir les différents fichiers JSON qui apparaissent dans Network. 
  - Comparer avec l'affichage du site pour déterminer quel est le bon.
  - Ajouter l'adresse au script `check.py`

## Installation

```shell
python -m venv env
source env/bin/activate
pip install telegram-send requests
telegram-send --configure
## enter your token (/newbot to @BotFather)
cp check.timer ~/.config/systemd/user/
cp check.service ~/.config/systemd/user/
```

## Activate Systemd timer

```
systemctl --user enable --now check.timer
```

## Testing

```
bash check.sh
```
