import picamera
import time
from RPi import GPIO


def provision_pi_camera(hflip=False, vflip=False, zoom=(0.0, 0.0, 1.0, 1.0), video_stabilization=True):
    camera = picamera.PiCamera()
    camera.hflip = hflip
    camera.vflip = vflip
    camera.video_stabilization = video_stabilization
    camera.zoom = zoom
    return camera


def initialize_gpio_pins():
    print("This is where we set our input pins and output pins for LEDs, motion sensor, and servo")


def rotate_servo(angle):
    print("This is where we would rotate the servo {} degrees.".format(angle))


def reset_servo():
    rotate_servo(0)


def turn_on_flood_light():
    print("This is where we would turn the LED array on.")


def main():
    camera = provision_pi_camera()
    camera.start_recording("test.h264")
    camera.wait_recording(10)
    camera.stop_recording()

if __name__ == "__main__":
    main()
