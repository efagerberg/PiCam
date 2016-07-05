#from gpiozero import MotionSensor
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)

##Send an email upon motion detecion

#pir = MotionSensor(4)

while(True):
	i = GPIO.input(11)
	if i==1:
    		print 'motion detected' , i
		time.sleep(4.1)
