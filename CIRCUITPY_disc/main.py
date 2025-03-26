import time
import board
import pwmio
import digitalio
from adafruit_motor import motor

import ir_decode

PWM_M1A = board.GP8
PWM_M1B = board.GP9
PWM_M2A = board.GP10
PWM_M2B = board.GP11

# DC motor setup
M1A = pwmio.PWMOut(PWM_M1A, frequency=10000)
M1B = pwmio.PWMOut(PWM_M1B, frequency=10000)
M2A = pwmio.PWMOut(PWM_M2A, frequency=10000)
M2B = pwmio.PWMOut(PWM_M2B, frequency=10000)
motor1 = motor.DCMotor(M1A, M1B)
motor2 = motor.DCMotor(M2A, M2B)


# Initialize buttons
btn1 = digitalio.DigitalInOut(board.GP20)
btn2 = digitalio.DigitalInOut(board.GP21)
btn1.direction = digitalio.Direction.INPUT
btn2.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.UP
btn2.pull = digitalio.Pull.UP


print("\n"*5)
print("Merles Auto :-)")


def handle_key_code(key_code):
    print("key_code", key_code)
    mydecoder.print_key_name(key_code)
    if key_code == ir_decode.key_codes["on"]:
        motor1.throttle = 1.0
        motor2.throttle = 1.0
    elif key_code == ir_decode.key_codes["off"]:
        motor1.throttle = 0.0
        motor2.throttle = 0.0
    elif key_code == ir_decode.key_codes["brightness_up"]:
        motor1.throttle = 1.0
        motor2.throttle = 0.5
    elif key_code == ir_decode.key_codes["brightness_down"]:
        motor1.throttle = 0.5
        motor2.throttle = 1.0
        pass
    elif key_code == ir_decode.key_codes["red"]:
        pass
    elif key_code == ir_decode.key_codes["blue"]:
        pass
    elif key_code == ir_decode.key_codes["green"]:
        pass
    elif key_code == ir_decode.key_codes["white"]:
        motor1.throttle = -1.0
        motor2.throttle = -1.0


mydecoder = ir_decode.IRDecode(callback=handle_key_code)

while True:
    mydecoder.update()

    # Check button 1 (GP20)
    if not btn1.value:  # button 1 pressed
        print("\nForwards slow")
        motor1.throttle = 0.9
        motor2.throttle = 0.5
        time.sleep(2)
        print("\nStop")
        motor1.throttle = 0
        motor2.throttle = 0 

    if not btn2.value:  # button 1 pressed
        print("\nBackwards slow")
        motor1.throttle = -0.9
        motor2.throttle = -0.9
        time.sleep(2)

        print("\nStop")
        motor1.throttle = 0
        motor2.throttle = 0
