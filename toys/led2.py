#!/usr/bin/env python

# Randomly blink LEDs attached to GPIO pins according to set ratio
# 18 == green
# 23 == red
# 22 == blue
import RPi.GPIO as GPIO, time, random, signal, sys

# clean up GPIO on caught signal
def signal_handler(signal, frame):
    GPIO.cleanup()
    sys.exit(0)

# Catch ctrl+C and cleanup
signal.signal(signal.SIGINT, signal_handler)

GPIO.setmode(GPIO.BCM)
GREEN_LED = 18
RED_LED = 23
BLUE_LED = 22
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(BLUE_LED, GPIO.OUT)

# only turn on if random number is higher than set value
blue = 0.3
red = 0.6
green = 0.9

while True:
    GPIO.output(BLUE_LED, random.random() > blue)
    GPIO.output(RED_LED, random.random() > red)
    GPIO.output(GREEN_LED, random.random() > green)
    time.sleep(1)
