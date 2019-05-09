#!/usr/bin/env python

# Allison Creely, 2018, LGPLv3 License
# Rock 64 GPIO Library for Python

import R64.GPIO as GPIO
from time import sleep


# Set Variables
var_gpio_out = 16


# GPIO Setup
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(var_gpio_out, GPIO.OUT, initial=GPIO.HIGH)       # Set up GPIO as an output, with an initial state of HIGH


# Test Output
print("")
print("Testing GPIO Input/Output:")

while True:
    print("On")
    GPIO.output(var_gpio_out, GPIO.HIGH)
    sleep(1)
    print("Off")
    GPIO.output(var_gpio_out, GPIO.LOW)
    sleep(1)





