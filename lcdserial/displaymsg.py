import sys
import collections

from pingo.parts import serial

DEFAULT_PORT = '/dev/ttyAMA0'  # the mini-UART port on the Raspberry Pi

def main(port=DEFAULT_PORT):
    lcd = serial.LCD16x2(port)
    print(lcd)
    lcd.clear()
    lines = collections.deque(['',''], 2)
    while True:
        lines.append(raw_input('> '))
        for i, line in enumerate(lines):
            lcd.set_cursor(i, 0)
            lcd.write(line.ljust(16, b' '))

if __name__ == '__main__':
    main(*sys.argv[1:])
