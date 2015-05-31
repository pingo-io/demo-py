from __future__ import print_function

import pingo

def pin_loc(pin):
    return int(pin.location)

rpi = pingo.rpi.RaspberryPi()

for pin in rpi.digital_pins:
    pin.mode = pingo.OUT
    pin.low()

pin_segment = []
for pin in sorted(rpi.digital_pins, key=pin_loc):
    pin.high()
    segment = raw_input('Lit: pin %s, segment:' % pin.location)
    if segment:
        pin_segment.append((pin.location, segment))
    pin.low()

for loc, seg in pin_segment:
    print(loc, seg)
