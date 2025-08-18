#!/bin/sh

/bin/sh ./detect-os.sh

if [ -d "/opt/khaos-bot/plugins" ]; then
    cp /opt/khaos-bot/plugins/*.py /app/bot/plugins
fi

if [ -f "/opt/khaos-bot/plugins/requirements.txt" ]; then
    pip3 install -r /opt/khaos-bot/plugins/requirements.txt
else
    touch /opt/khaos-bot/plugins/requirements.txt
fi

python3 /app/main.py