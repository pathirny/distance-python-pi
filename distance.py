import RPi.GPIO as GPIO
from gpiozero import DistanceSensor
import time

# set the trigger and echo pin

PIN_TRIGGER = 4
PIN_ECHO = 17
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)



GPIO.setup(PIN_TRIGGER, GPIO.OUT)
GPIO.setup(PIN_ECHO, GPIO.IN)

def distance():
# GPIO.setup(27, GPIO.OUT)
# GPIO.output(27, GPIO.HIGH)
# time.sleep(1)
# GPIO.output(27, GPIO.LOW)
    GPIO.output(PIN_TRIGGER, True)

    # print("Waiting for sensor...")
    # time.sleep(2)

    # print("Calculating distance...")

    GPIO.output(PIN_TRIGGER, False)

    startTime =  time.time()
    endTime = time.time()
    while GPIO.input(PIN_ECHO) == 0:
        startTime = time.time()
    while GPIO.input(PIN_ECHO) == 1:
        endTime = time.time()

    duration = endTime - startTime

    distance = (duration * 34300) / 2

    return distance

try:
    while True: 
        dist= distance()
        print(f"Measured distance = {dist}cm")
        time.sleep(1)
finally:
    if KeyboardInterrupt == True:
        print("Measurement Stopped by user")
        GPIO.cleanup()

