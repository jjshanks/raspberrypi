#!/usr/bin/env python

import time, sys, singal
import RPi.GPIO as GPIO
import datetime as dt

# This read triggers and reads the signal from a HC-SR04 unit and 
# displays the value in inches.

# usage: sudo python hc-sr04.py [reading delay]

# DATASHEET: https://docs.google.com/document/d/1Y-yZnNhMYy7rwhAgyL_pfa39RsB-x2qR4vP8saG73rE/edit

# clean up GPIO on caught signal
def signal_handler(signal, frame):
    GPIO.cleanup()
    sys.exit(0)

# Catch ctrl+C and cleanup
signal.signal(signal.SIGINT, signal_handler)

GPIO.setmode(GPIO.BCM)

TRIG = 25
ECHO = 24

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
#ensure trigger signal is low
GPIO.setup(TRIG, GPIO.LOW)

def reading():
    # pulse for 10 microseconds to start a reading
    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(TRIG, GPIO.LOW)

    signalStart = signalStop = None
    # time the start and stop of the signal on echo line
    # safe guard against looping forever
    for x in xrange(10000):
        echo = GPIO.input(ECHO)
        if echo:
            signalStart = time.time()
            break

    for x in xrange(10000):
        echo = GPIO.input(ECHO)
        if not echo:
            signalStop = time.time()
            break

    # if reading failed return None
    if signalStop == None or signalStart == None:
        return None

    signalTime = signalStop - signalStart

    # Dividing by 0.000148 gives inches
    return signalTime / 0.000148

delay = 0.5
if len(sys.argv) > 1:
    delay = float(sys.argv[1])

while True:
    print reading()
    time.sleep(delay)
