import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

def blink(output, speed):
    GPIO.output(output,True)
    time.sleep(speed)
    GPIO.output(output,False)
    time.sleep(speed)

for i in range(50):
    blink(7, 0.05)
    blink(11, 0.05)
    blink(15, 0.05)
GPIO.cleanup()

