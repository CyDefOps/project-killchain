#!/bin/bash
SERVER_IP="{your_server_ip}"
SERVER_PORT=8448
TIMEOUT=5
IFTTT_WEBHOOK_URL="https://maker.ifttt.com/trigger/{your_trigger}/with/key/{your_key}"

nc -z -v -w$TIMEOUT $SERVER_IP $SERVER_PORT

if [ $? -eq 0 ]; then
    echo "The Matrix homeserver is online."
else
    echo "The Matrix homeserver is offline."
    curl -X POST $IFTTT_WEBHOOK_URL
fi
