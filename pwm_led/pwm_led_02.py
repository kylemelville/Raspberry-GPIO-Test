import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

p0 = GPIO.PWM(7, 50)
p1 = GPIO.PWM(13, 50)
p2 = GPIO.PWM(29, 50)
p0.start(0)
p1.start(0)
p2.start(0)
try:
    while True:
        for i in range(100):
			p0.ChangeDutyCycle(i)
            p1.ChangeDutyCycle(i)
            p2.ChangeDutyCycle(i)
            time.sleep(0.02)
        for i in range(100):
            p0.ChangeDutyCycle(100 - i)
            p1.ChangeDutyCycle(100 - i)
            p2.ChangeDutyCycle(100 - i)
            time.sleep(0.02)
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()
