import time

from pingo.parts import serial

lcd = serial.LCD16x2('/dev/ttyAMA0', 9600)

while True:
    lcd.move_cursor(0, 0)
    lcd.write(time.strftime('%H:%M:%S'))
    time.sleep(1)
