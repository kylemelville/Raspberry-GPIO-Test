import RPi.GPIO as GPIO
import time
import math

#variables
min = 0
max = 100

#functions
def draw_leds(h):
    for i in range(len(leds)):
        y = -22 * math.pow(i - h, 2) + max
        if y < min:
            y = 0
        elif y > max:
            y = 100
        leds[i].ChangeDutyCycle(y)

def get_new_led(pin, frequency):
    GPIO.setup(pin, GPIO.OUT)
    return GPIO.PWM(pin, frequency)

def toggle_leds(mode):
    if mode:
        for led in leds:
            led.start(0)
    else:
        for led in leds:
            led.stop(0)

#execution
GPIO.setmode(GPIO.BOARD)
leds = []
leds.append(get_new_led(7, 50))
leds.append(get_new_led(11, 50))
leds.append(get_new_led(13, 50))
leds.append(get_new_led(15, 50))
leds.append(get_new_led(29, 50))
leds.append(get_new_led(31, 50))
leds.append(get_new_led(33, 50))
toggle_leds(True)
try:
    while True:
        for i in range(len(leds)):
            time.sleep(0.1)
            draw_leds(i)
        for i in range(len(leds) - 1, -1, -1):
            time.sleep(0.1)
            draw_leds(i)
except KeyboardInterrupt:
    pass
toggle_leds(False)
GPIO.cleanup()
