import pingo

board = pingo.detect.get_board()

led_pins = [24, 21, 23]
led_pins = [board.pins[i] for i in led_pins]
for pin in led_pins:
    pin.mode = pingo.OUT

rgb = pingo.parts.led.RGBLed(*led_pins)

while True:
    rgb.cycle()
