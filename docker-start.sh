#!/bin/sh

if [ -f /etc/ip-bot/requirements.txt ]; then
    pip3 install -r /etc/ip-bot/requirements.txt
fi

if [ -d /etc/ip-bot/plugins ]; then
    cp -r /etc/ip-bot/plugins/* /app/bot/plugins/
fi

python3 /app/main.py