import time
import sys

from pingo.parts import serial

DEFAULT_PORT = '/dev/ttyAMA0'  # the mini-UART port on the Raspberry Pi

def main(port=DEFAULT_PORT):
    lcd = serial.LCD16x2(port)
    lcd.clear()
    lcd.set_cursor(0, 0)
    lcd.write(b'Pingo = Pin, go!')

    while True:
        lcd.set_cursor(1, 4)
        lcd.write(time.strftime('%H:%M:%S'))
        time.sleep(1)

if __name__ == '__main__':
    main(*sys.argv[1:])
