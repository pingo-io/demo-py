import sys

from pingo.parts import serial

DEFAULT_PORT = '/dev/ttyAMA0'  # the mini-UART port on the Raspberry Pi

def main(port=DEFAULT_PORT):
    lcd = serial.LCD16x2(port)
    while True:
        lcd.clear()
        lcd.set_cursor(0, 0)
        msg = raw_input('> ')
        lcd.write(msg)

if __name__ == '__main__':
    main(*sys.argv[1:])
