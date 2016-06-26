from gpiozero import MotionSensor

##Send an email upon motion detecion

pir = MotionSensor(4)
i = 0
while(i < 1):
    if pir.motion_detected:
        print i , 'motion detected'
        execfile("send_email.py")
        i+=1;