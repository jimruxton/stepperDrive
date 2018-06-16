#!/usr/bin/python3
# Filename: rangeFind.py

# sample script to read range values from Maxbotix ultrasonic rangefinder
# note only worked with hardware uart on PI3 so be sure to configure it properly

from time import sleep
import maxSonarTTY

serialPort = "/dev/ttyAMA0"
maxRange = 5000  # change for 5m vs 10m sensor
sleepTime = 1 # time between measurements
minMM = 9999
maxMM = 0

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
    sleep(sleepTime)
