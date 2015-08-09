import time
import pingo
import itertools

rpi = pingo.detect.get_board()

msg = 'This demo requires a Raspberry Pi 2 B board'
assert rpi.__class__.__name__ == 'RaspberryPi2B', msg

gpio_leds = [18, 23, 24, 25, 12, 16, 20, 21]
led_pins = [rpi.gpio[n] for n in gpio_leds]

for pin in led_pins:
    pin.mode = pingo.OUT

try:
    while True:
        for pin in itertools.cycle(led_pins):
            pin.high()
            time.sleep(.1)
            pin.low()
finally:
    for pin in led_pins:
        pin.low()




