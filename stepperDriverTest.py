from time import sleep
import RPi.GPIO as GPIO

DIR = 20   # Direction GPIO Pin
STEP = 21  # Step GPIO Pin
CW = 0    # Clockwise Rotation
CCW = 1    # Counterclockwise Rotation
SPR = 5373   # Steps per Revolution (360 / .067)

GPIO.setmode(GPIO.BCM)
#GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# testing GIT
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(STEP, 0)
sleep(3)
GPIO.output(STEP, 1)
sleep(3)
GPIO.output(STEP, 0)
sleep(3)
GPIO.output(STEP, 1)
sleep(3)


GPIO.cleanup()
