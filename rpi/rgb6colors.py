import pingo

board = pingo.detect.get_board()

led_pins = [board.pins[i] for i in [24, 23, 21]]

for pin in led_pins:
    pin.mode = pingo.OUT

rgb = pingo.parts.led.RGBLed(*led_pins)

while True:
    for color, _ in pingo.parts.led.PURE_COLORS:
        rgb.color = color
        raw_input(color)
