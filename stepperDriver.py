from time import sleep
import RPi.GPIO as GPIO

DIR = 20  # Direction GPIO Pin
STEP = 21  # Step GPIO Pin
CW = 1    # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
SPR = 5373*2   # Steps per Revolution (360 / .067)
cycles=1000

GPIO.setmode(GPIO.BCM)
#GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# testing GIT
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR, CW)

step_count = SPR
delay = .001
#delay = .0000001
for y in range(cycles):
    GPIO.output(DIR, CW)
    for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)

 #   sleep(.3)
 #   GPIO.output(DIR, CCW)
 #   for x in range(step_count):
 #       GPIO.output(STEP, GPIO.HIGH)
 #       sleep(delay)
 #       GPIO.output(STEP, GPIO.LOW)
 #       sleep(delay)
 #   sleep(.3)

GPIO.cleanup()
