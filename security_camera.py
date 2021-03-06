import picamera
from RPi import GPIO
import os
import base64
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail. Attachment, Email, Content
from gpiozero import MotionSensor
from datetime import datetime
import time

SERVO_PIN = 13
MOTION_PIN = 11


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
    time.sleep(1.5)


def reset_servo():
    rotate_servo(90)


def send_email(*filenames):
    # This function will need to take in pictures and add them as attachments.
    sg = SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    print os.environ.get('SENDGRID_API_KEY')
    from_email = Email("SpyPi@no-reply")
    subject = "Motion Detected"
    to_email = Email("gagnej3@wit.edu")
    content = Content("text/plain", "We have detected motion from your pi!\n\n")
    mail = Mail(from_email, subject, to_email, content)

    for filename in filenames:
        with open(filename, "rb") as jpg_file:
            attachment = Attachment()
            attachment.set_filename(filename)
            attachment.set_content(base64.b64encode(jpg_file.read()))
            attachment.set_type('image/jpg')
            mail.add_attachment(attachment)

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
    GPIO.setup(MOTION_PIN, GPIO.IN)
    with provision_pi_camera() as camera:
        while True:
            i = GPIO.input(MOTION_PIN)
        if i == 1:
            print 'motion detected'
        pwm.ChangeDutyCycle(7)
        time.sleep(1)
        now = datetime.now()
        middle_filename = "{}-middle.jpg".format(now.isoformat())
        camera.capture(middle_filename)
        pwm.ChangeDutyCycle(2)
        time.sleep(1.5)
        left_filename = "{}-left.jpg".format(now.isoformat())
        camera.capture(left_filename)
        pwm.ChangeDutyCycle(7)
        time.sleep(1.5)
        right_filename = "{}-right.jpg".format(now.isoformat())
        camera.capture(right_filename)
        pwm.ChangeDutyCycle(12)
        time.sleep(1.5)
        pwm.ChangeDutyCycle(7)
        send_email(middle_filename, left_filename, right_filename)


if __name__ == "__main__":
    main()
