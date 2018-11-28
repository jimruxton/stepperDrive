from time import sleep
import RPi.GPIO as GPIO
import maxSonarTTY
from time import time
from serial import Serial
serialPort = "/dev/ttyAMA0" # default for RaspberryPi
maxRange = 5000  # change for 5m vs 10m sensor
sleepTime = 1 # time between measurements
minMM = 9999
maxMM = 0
DIR = 20  # Direction GPIO Pin
STEP = 21  # Step GPIO Pin
CW = 0    # Clockwise Rotation
CCW = 1    # Counterclockwise Rotation
SPR = 5373*2   # Steps per Revolution (360 / .067)
cycles=5

GPIO.setmode(GPIO.BCM)
#GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# testing GIT
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR, CCW)

step_count = SPR
#delay = .001
#delay = .0000001
delay = .001

while True:
    mm = maxSonarTTY.measure(serialPort)
    if mm >= maxRange:
        print("no target")
        sleep(sleepTime)
        continue
    if mm < minMM:
        minMM = mm
    if mm > maxMM:
        maxMM = mm
    print("distance:", mm, "  min:", minMM, "max:", maxMM)
    if mm < 500:
        for y in range(cycles):
            GPIO.output(DIR, CCW)
            for x in range(step_count):
                GPIO.output(STEP, GPIO.HIGH)
                sleep(delay)
                GPIO.output(STEP, GPIO.LOW)
                sleep(delay)


GPIO.cleanup()
