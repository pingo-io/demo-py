import time

import pingo

#           A   B   C   D   E  F  G  dp
SEGMENTS = [7, 11, 18, 16, 12, 5, 3, 22]

rpi = pingo.rpi.RaspberryPi()

pins = [rpi.pins[n] for n in SEGMENTS]

for pin in pins:
    pin.mode = pingo.OUT
    pin.low()

for pin in pins:
    pin.high()
    time.sleep(1)
