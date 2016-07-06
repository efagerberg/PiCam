import picamera
from RPi import GPIO
import os
import sendgrid
from sendgrid.helpers.mail import Email, Content, Mail
from gpiozero import MotionSensor
from datetime import datetime
import time

SERVO_PIN = 13


def provision_pi_camera(hflip=False, vflip=False, zoom=(0.0, 0.0, 1.0, 1.0), video_stabilization=True):
    camera = picamera.PiCamera()
    camera.hflip = hflip
    camera.vflip = vflip
    camera.video_stabilization = video_stabilization
    camera.zoom = zoom
    return camera


def rotate_servo(angle):
    DC = 0
    if angle == 90:
        DC = 7
    elif angle == 0:
        DC = 2
    elif angle == 180:
        DC = 12
    else:
        raise ValueError("Accepted values for servo rotation are 0, 90, and 180.")

    pwm = GPIO.PWM(SERVO_PIN, 50)
    pwm.ChangeDutyCycle(DC)   # turn towards 90 degree
    time.sleep(1)            # sleep 1 second


def reset_servo():
    rotate_servo(90)


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
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(SERVO_PIN, GPIO.OUT)
    # pwm object on servo pin with 50Hz signal
    pwm = GPIO.PWM(SERVO_PIN, 50)
    pwm.start(7)
    # ----------End of Servo Setup -------------
    pir = MotionSensor(4)
    with provision_pi_camera() as camera:
        while True:
            if pir.motion_detected:
                now = datetime.now()
                camera.capture("{}-middle.jpg".format(now.iso_format()))
                rotate_servo(0)
                camera.capture("{}-left.jpg".format(now.iso_format()))
                rotate_servo(180)
                camera.capture("{}-right.jpg".format(now.iso_format()))
                reset_servo()
                send_email()


if __name__ == "__main__":
    main()
