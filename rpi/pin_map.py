import pingo

FMT = '{:>22} {:>2} {:<2} {}'

def order_key(loc_pin_pair):
    loc, pin = loc_pin_pair
    return int(loc)

rpi = pingo.rpi.RaspberryPi2B()

for loc1, pin1 in sorted(rpi.pins.items(), key=order_key)[::2]:
    loc2 = int(loc1) + 1
    pin2 = rpi.pins[loc2]
    print FMT.format(pin1, loc1, loc2, pin2)
