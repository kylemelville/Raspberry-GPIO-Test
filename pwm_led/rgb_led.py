import RPi.GPIO as GPIO
import time

#variables
colors = [] #[red, green, blue]

#functions
def set_RGB(R, G, B, delay):
    colors[0].ChangeDutyCycle(R)
    colors[1].ChangeDutyCycle(G)
    colors[2].ChangeDutyCycle(B)
    time.sleep(delay)

def get_new_color(pin, frequency):
    GPIO.setup(pin, GPIO.OUT)    
    return GPIO.PWM(pin, frequency)

def start_colors():
    for color in colors:
        color.start(0)

def stop_colors():
    for color in colors:
        color.stop(0)

#execution
GPIO.setmode(GPIO.BOARD)
colors.append(get_new_color(33, 100))
colors.append(get_new_color(35, 100))
colors.append(get_new_color(37, 100))
start_colors()
try:
    while True:
        for i in range(0, 100, 5):
            set_RGB(i, i, i, 0.05)
        for i in range(100, 0, -5):
            set_RGB(i, i, i, 0.05)
except KeyboardInterrupt:
    pass
stop_colors()
GPIO.cleanup()
