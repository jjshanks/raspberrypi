#!/usr/bin/env python

import time, sys, signal
import RPi.GPIO as GPIO
import datetime as dt

# This turns on an LED when motion is detected by an HC-SR501 unit
# and keeps it on until no motion is detected for 10 or the passed in
# number of seconds

# usage: sudo python hc-sr501.py [hold time]

# DATASHEET: http://www.mpja.com/download/31227sc.pdf

# clean up GPIO on caught signal
def signal_handler(signal, frame):
    GPIO.cleanup()
    sys.exit(0)

# Catch ctrl+C and cleanup
signal.signal(signal.SIGINT, signal_handler)

GPIO.setmode(GPIO.BCM)

SIG = 23
LED = 18

GPIO.setup(SIG, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

hold_for = 10
if len(sys.argv) > 1:
    hold_for = float(sys.argv[1])

hold_till = time.time()
GPIO.output(LED, False)

while True:
    current = GPIO.input(SIG)
    # turn on LED and update hold time
    if current == 1:
        GPIO.output(LED, True)
        hold_till = time.time() + hold_for
    # otherwise if it is past the hold time switch off LED
    elif time.time() > hold_till:
        GPIO.output(LED, False)
    time.sleep(0.1)
