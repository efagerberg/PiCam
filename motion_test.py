from gpiozero import MotionSensor

##Quick script to check communication between motion sensor and Pi on GPIO 4.

pir = MotionSensor(4)
i = 0
while(i < 5):
    if pir.motion_detected:
        print i , 'motion detected'
        i+=1;