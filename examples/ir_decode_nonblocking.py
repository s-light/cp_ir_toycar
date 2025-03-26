import board
import pulseio
import neopixel
import adafruit_irremote

import digitalio

print("")
print("ir_decode_nonblocking.py")

pulsein = pulseio.PulseIn(board.GP3, maxlen=120, idle_state=True)
# decoder = adafruit_irremote.GenericDecode()
decoder = adafruit_irremote.NonblockingGenericDecode(pulsein)


def read_command():
    """Try to read an IR command. If none seen or if error, return None."""
    # based on https://github.com/adafruit/Adafruit_CircuitPython_IRRemote/blob/main/examples/irremote_nonblocking.py
    for message in decoder.read():
        print("Heard", len(message.pulses), "Pulses:", message.pulses)
        if isinstance(message, adafruit_irremote.IRMessage):
            print("Decoded:", message.code)
        elif isinstance(message, adafruit_irremote.NECRepeatIRMessage):
            print("NEC repeat!")
            pass
        elif isinstance(message, adafruit_irremote.UnparseableIRMessage):
            print("Failed to decode", message.reason)
        print("----------------------------")

def main():
    read_command()


while True:
    main()
