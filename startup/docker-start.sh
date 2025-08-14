#!/bin/sh


if [ ! -d "/etc/khaos-bot/plugins" ]; then
    mkdir -p /etc/khaos-bot/plugins
fi

if [ -f "/etc/khaos-bot/plugins/requirements.txt" ]; then
    pip3 install -r /etc/khaos-bot/plugins/requirements.txt
else
    touch /etc/khaos-bot/plugins/requirements.txt
fi


python3 /app/main.py