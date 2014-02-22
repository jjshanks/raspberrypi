#!/usr/bin/env python

# Randomly blink LEDs attached to GPIO pins 18 (green) and 23 (red)
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
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)

while True:
    GPIO.output(GREEN_LED, True)
    GPIO.output(RED_LED, False)
    time.sleep(random.random())
    GPIO.output(GREEN_LED, False)
    GPIO.output(RED_LED, True)
    time.sleep(random.random())
    GPIO.output(GREEN_LED, False)
    GPIO.output(RED_LED, False)
    time.sleep(random.random())
