# Installation

```shell
python -m venv env
source env/bin/activate
pip install telegram-send requests
telegram-send --configure
## enter your token (/newbot to @BotFather)
cp check.timer ~/.config/systemd/user/
cp check.service ~/.config/systemd/user/
```

# Activate Systemd timer

```
systemctl --user enable --now check.timer
```
