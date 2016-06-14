import RPi.GPIO as GPIO
import time

#functions
def toggle_leds(mode):
    if mode:
        for led in leds:
            led.start(0)
    else:
        for led in leds:
            led.stop(0)

def get_new_led(pin, frequency):
    GPIO.setup(pin, GPIO.OUT)
    return GPIO.PWM(pin, frequency)

#execution
GPIO.setmode(GPIO.BOARD)
leds = []
leds.append(get_new_led(7, 50))
leds.append(get_new_led(13, 50))
leds.append(get_new_led(29, 50))
toggle_leds(True)
try:
    while True:
        for i in range(100):
            for led in leds:
                led.ChangeDutyCycle(i)
            time.sleep(0.02)
        for i in range(100):
            for led in leds:
                led.ChangeDutyCycle(100 - i)
            time.sleep(0.02)
except KeyboardInterrupt:
    pass
toggle_leds(False)
GPIO.cleanup()