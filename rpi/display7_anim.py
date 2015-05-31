from time import sleep

import pingo

#           A   B   C   D   E  F  G  dp
SEGMENTS = [7, 11, 18, 16, 12, 5, 3, 22]

rpi = pingo.rpi.RaspberryPi()

pins = [rpi.pins[loc] for loc in SEGMENTS]

for pin in pins:
    pin.mode = pingo.OUT
    pin.low()

while True:
    for pin in pins[:6]:
        pin.high()
        sleep(.04)
        pin.low()
