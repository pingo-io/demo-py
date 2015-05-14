#!/usr/bin/env python2.7

import time
import sys

from pingo.parts import serial

DEFAULT_PORT = '/dev/ttyAMA0'  # the mini-UART port on the Raspberry Pi

def main(msg='', port=DEFAULT_PORT):
    lcd = serial.LCD16x2(port)
    lcd.clear()
    lcd.set_cursor(0, 0)
    timestr = time.strftime('booted: %H:%M:%S') 
    lcd.write(timestr.center(16))
    lcd.set_cursor(1, 0)
    lcd.write(msg.center(16))


if __name__ == '__main__':
    main(*sys.argv[1:])
