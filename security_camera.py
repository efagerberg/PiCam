import picamera
from RPi import GPIO
import sendgrid
import os
from sendgrid.helpers.mail import *
from gpiozero import MotionSensor
from datetime import datetime


def provision_pi_camera(hflip=False, vflip=False, zoom=(0.0, 0.0, 1.0, 1.0), video_stabilization=True):
    camera = picamera.PiCamera()
    camera.hflip = hflip
    camera.vflip = vflip
    camera.video_stabilization = video_stabilization
    camera.zoom = zoom
    return camera


def rotate_servo(angle):
	servoPin = 18

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(servoPin, GPIO.OUT)

	#pwm object on servo pin with 50Hz signal
    pwm = GPIO.PWM(servoPin, 50)
    pwm.start(7)

    DC = float(1 / 18) * (angle) + 2
    pwm.ChangeDutyCycle(DC)


def reset_servo():
    rotate_servo(0)


def turn_on_flood_light():
    print("This is where we would turn the LED array on.")


def send_email():
    # This function will need to take in pictures and add them as attachments.
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("SpyPi@no-reply")
    subject = "Motion Detected"
    to_email = Email("sendToUser@example.com")
    content = Content("text/plain", "We have detected motion from your pi!\n\n")
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)


def main():
    pir = MotionSensor(4)
    with provision_pi_camera() as camera:
        while True:
            if pir.motion_detected:
                now = datetime.now()
                camera.capture("{}-initial.jpg".format(now.iso_format()))
                turn_on_flood_light()
                rotate_servo(0)
                camera.capture("{}-left.jpg".format(now.iso_format()))
                rotate_servo(90)
                camera.capture("{}-middle.jpg".format(now.iso_format()))
                rotate_servo(180)
                camera.capture("{}-right.jpg".format(now.iso_format()))
                reset_servo()
                send_email()


if __name__ == "__main__":
    main()
