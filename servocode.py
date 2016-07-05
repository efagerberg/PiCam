import RPi.GPIO as GPIO
import time

servoPin = 13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPin, GPIO.OUT)

# pwm object on servo pin with 50Hz signa
pwm = GPIO.PWM(servoPin, 50)
pwm.start(7)

try:
    while True:
        pwm.ChangeDutyCycle(7)   # turn towards 90 degree
        time.sleep(1)            # sleep 1 second
        pwm.ChangeDutyCycle(2)   # Turn toward 0 degree
        time.sleep(1)		     # sleep 1 second
        pwm.ChangeDutyCycle(7)
        time.sleep(1)
        pwm.ChangeDutyCycle(12)  # turn toward 180 degree
        time.sleep(1)            # sleep 1 second

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
