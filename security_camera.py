import picamera
import time
from RPi import GPIO


def provision_pi_camera(hflip=False, vflip=False, zoom=0, visual_stabilization=True):
    camera = picamera.PiCamera()
    camera.hflip = hflip
    camera.vflip = vflip
    camera.visual_stabilization
    camera.zoom = 0


def initialize_gpio_pins():
    print "This is where we set our input pins and output pins for LEDs, motion sensor, and servo"


def rotate_servo(angle):
    print "This is where we would rotate the servo {} degrees.".format(angle)


def reset_servo():
    rotate_servo(0)


def turn_on_flood_light():
    print "This is where we would turn the LED array on."


def main():
    with provision_pi_camera() as camera:
        camera.start_preview()
        time.sleep(10)
        camera.stop_preview()

if __name__ == "__main__":
    main()
