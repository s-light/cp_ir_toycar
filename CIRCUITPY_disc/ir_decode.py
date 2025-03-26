import board
import pulseio
import neopixel
import adafruit_irremote

import digitalio

key_codes = {
    "brightness_up": (0, 255, 1, 254),
    "brightness_down": (0, 255, 129, 126),
    "off": (0, 255, 65,190),
    "on": (0, 255, 193, 62),

    "white": (0, 255, 225,30),
    
    "flash": (0, 255, 209,46),
    "strobe": (0, 255, 241,14),
    "fade": (0, 255, 201,54),
    "smooth": (0, 255, 233,22),
    
    "red": (0, 255, 33,222),
    "green": (0, 255, 161,94),
    "blue": (0, 255, 97,158),

    "orange_1": (0, 255, 17,238),
    "orange_2": (0, 255, 49,206),
    "orange_3": (0, 255,9,246 ),
    "orange_4": (0, 255, 41,214),
    "green_1": (0, 255, 145,110),
    "green_2": (0, 255,177,78 ),
    "green_3": (0, 255,137,118),
    "green_4": (0, 255,169,86),
    "blue_1": (0, 255,81,174),
    "blue_2": (0, 255,113,142),
    "blue_3": (0, 255,73,182),
    "blue_4": (0, 255,105,150),
}

class IRDecode:
    def __init__(self, *, callback=None):

        if callback is None:
            callback = self.handle_key_code
        self.callback = callback

        # ir_VCC = digitalio.DigitalInOut(board.A2)
        # ir_VCC.direction = digitalio.Direction.OUTPUT
        # ir_VCC.value = True

        # ir_GND = digitalio.DigitalInOut(board.A3)
        # ir_GND.direction = digitalio.Direction.OUTPUT
        # ir_GND.value = False

        pulsein = pulseio.PulseIn(board.GP3, maxlen=120, idle_state=True)

        # decoder = adafruit_irremote.GenericDecode()
        self.decoder = adafruit_irremote.NonblockingGenericDecode(pulsein)

    def update(self):
        """Try to read an IR command. If none seen or if error, return None."""
        # based on https://github.com/adafruit/Adafruit_CircuitPython_IRRemote/blob/main/examples/irremote_nonblocking.py
        for message in self.decoder.read():
            # print("Heard", len(message.pulses), "Pulses:", message.pulses)
            if isinstance(message, adafruit_irremote.IRMessage):
                print("Decoded:", message.code)
                self.callback(message.code)
            elif isinstance(message, adafruit_irremote.NECRepeatIRMessage):
                # print("NEC repeat!")
                pass
            elif isinstance(message, adafruit_irremote.UnparseableIRMessage):
                print("Failed to decode", message.reason)
            # print("----------------------------")

    def  get_key_name(self, key_code):
        try:
            key_name = list(key_codes.keys())[list(key_codes.values()).index(key_code)]
        except ValueError as e:
            print(e)
        return key_name

    def  print_key_name(self, key_code):
        print(self.get_key_name(key_code))

    def  handle_key_code(self, key_code):
        print("key_code", key_code)
        self.print_key_name(key_code)
        if key_code == key_codes["on"]:
            pass
        elif key_code == key_codes["off"]:
            pass
        elif key_code == key_codes["brightness_up"]:
            pass
        elif key_code == key_codes["brightness_down"]:
            pass
        elif key_code == key_codes["red"]:
            pass
        elif key_code == key_codes["blue"]:
            pass
        elif key_code == key_codes["green"]:
            pass


def main():
    import time
    print("")
    print("ir_decode.py")
    ir_decode = IRDecode()
    while True:
        ir_decode.update()
        time.sleep(0)


# main()