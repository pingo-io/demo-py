#!/usr/bin/env python2.7

import time
import sys

from pingo.parts import serial

DEFAULT_PORT = '/dev/ttyAMA0'  # the mini-UART port on the Raspberry Pi

def main(msgs):
    lcd = serial.LCD16x2(DEFAULT_PORT)
    lcd.clear()
    for i, msg in enumerate(msgs[:2]):
        lcd.set_cursor(i, 0)
        lcd.write(msg)

if __name__ == '__main__':
    main(*sys.argv[1:])
