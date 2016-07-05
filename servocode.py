import RPi.GPIO as GPIO

def rotate_servo(angle):
	servoPin = 18

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(servoPin, GPIO.OUT)

	#pwm object on servo pin with 50Hz signal
    pwm = GPIO.PWM(servoPin, 50)
    pwm.start(7)

    DC = float(1 / 18) * (angle) + 2
    pwm.ChangeDutyCycle(DC)
