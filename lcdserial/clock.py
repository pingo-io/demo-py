import time
import datetime
import sys

from pingo.parts import serial

DEFAULT_PORT = '/dev/ttyAMA0'  # the mini-UART port on the Raspberry Pi

def main(port=DEFAULT_PORT):
    lcd = serial.LCD16x2(port)
    time.sleep(.5)  # wait for display to boot up
    lcd.clear()

    while True:
        lcd.set_cursor(0, 0)
        now = datetime.datetime.now()
        lcd.write(now.strftime('%H:%M:%S.%f')[:10])
        time.sleep(.1)

if __name__ == '__main__':
    main(*sys.argv[1:])
