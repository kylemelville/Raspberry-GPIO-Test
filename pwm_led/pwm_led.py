import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

p = GPIO.PWM(7, 50)
p.start(0)
try:
    while True:
        for i in range(100):
            p.ChangeDutyCycle(i)
            time.sleep(0.02)
        for i in range(100):
            p.ChangeDutyCycle(100 - i)
            time.sleep(0.02)
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()
