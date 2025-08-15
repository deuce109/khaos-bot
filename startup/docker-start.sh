#!/bin/sh


if [ -d "/etc/khaos-bot/plugins" ]; then
    cp /etc/khaos-bot/plugins/* /app/bot/plugins
fi

if [ -f "/etc/khaos-bot/plugins/requirements.txt" ]; then
    pip3 install -r /etc/khaos-bot/plugins/requirements.txt
else
    touch /etc/khaos-bot/plugins/requirements.txt
fi


python3 /app/main.py