# Installation

```shell
python -m venv env
source env/bin/activate
pip install telegram-send requests
telegram-send --configure
```

# Activate Systemd timer

```
systemctl --user enable --now check.timer
```