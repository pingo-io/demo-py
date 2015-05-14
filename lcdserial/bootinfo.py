#!/usr/bin/env python2.7

import time
import sys

from pingo.parts import serial

DEFAULT_PORT = '/dev/ttyAMA0'  # the mini-UART port on the Raspberry Pi

def main(*msgs):
    lcd = serial.LCD16x2(DEFAULT_PORT)
    lcd.clear()
    for i, msg in enumerate(msgs):
        lcd.set_cursor(i%2, 0)
        lcd.write(msg)
        if i > 1:
            time.sleep(.5)


if __name__ == '__main__':
    main(*sys.argv[1:])
