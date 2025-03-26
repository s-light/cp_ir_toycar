import time
import board
import pulseio
import neopixel
import adafruit_irremote

import digitalio

print("")
print("ir_pulse_test.py")

ir_SIG = digitalio.DigitalInOut(board.GP3)
ir_SIG.direction = digitalio.Direction.INPUT


def main():
    print(ir_SIG.value)
    time.sleep(0.01)


while True:
    main()
