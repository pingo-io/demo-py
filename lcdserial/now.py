#!/usr/bin/env python2.7

import time
import sys

from pingo.parts import serial

DEFAULT_PORT = '/dev/ttyAMA0'  # the mini-UART port on the Raspberry Pi

def main(msg='', port=DEFAULT_PORT):
    lcd = serial.LCD16x2(port)
    print(lcd)
    lcd.clear()
    lcd.set_cursor(0, 0)
    lcd.write(b'Pingo = Pin, go!')

    lcd.set_cursor(1, 0)
    timestr = time.strftime('%H:%M:%S')
    lcd.write((msg + ' '+timestr).center(16))

if __name__ == '__main__':
    main(*sys.argv[1:])
