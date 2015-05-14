#!/bin/sh -e
. /home/pi/pingo/.env27/bin/activate
TZ='America/Sao_Paulo'; export TZ
python /home/pi/pingo/demo-py/lcdserial/bootinfo.py `hostname -I`
