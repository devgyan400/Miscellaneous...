import RPi.GPIO as GPIO
import time
import os

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
DOPPLER_PIN = 11
GPIO.setup(DOPPLER_PIN,GPIO.IN)

def getspeed():
    NUM_CYCLES = 3
    GPIO.wait_for_edge(11, GPIO.FALLING)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
        GPIO.wait_for_edge(11, GPIO.FALLING)
    duration = time.time() - start
    frequency = NUM_CYCLES/duration
    speed = frequency / float(31.36)
    return speed

try:
    while True:
        if getspeed() > 1:
                print(getspeed())
except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()
