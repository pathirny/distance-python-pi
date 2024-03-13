import RPi.GPIO as GPIO
import time

# Set the GPIO mode and warnings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define the GPIO pins for LEDs and ultrasonic sensor
greenLed = 23
yellowLed = 22
redLed = 27
PIN_TRIGGER = 4
PIN_ECHO = 17

# Set up GPIO pins
GPIO.setup(redLed, GPIO.OUT)
GPIO.setup(yellowLed, GPIO.OUT)
GPIO.setup(greenLed, GPIO.OUT)
GPIO.setup(PIN_TRIGGER, GPIO.OUT)
GPIO.setup(PIN_ECHO, GPIO.IN)

def distance():
    GPIO.output(PIN_TRIGGER, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(PIN_TRIGGER, GPIO.LOW)

    startTime = time.time()
    endTime = time.time()

    while GPIO.input(PIN_ECHO) == 0:
        startTime = time.time()
    while GPIO.input(PIN_ECHO) == 1:
        endTime = time.time()

    duration = endTime - startTime
    distance = (duration * 34300) / 2

    print(distance)

# try:
#     while True:
#         dist = distance()
#         print(f"Measured distance = {dist} cm")
#         time.sleep(1)

#         if dist < 5:
#             GPIO.output(redLed, GPIO.HIGH)
#             GPIO.output(yellowLed, GPIO.LOW)
#             GPIO.output(greenLed, GPIO.LOW)
#         elif 5 <= dist < 20:
#             GPIO.output(redLed, GPIO.LOW)
#             GPIO.output(yellowLed, GPIO.HIGH)
#             GPIO.output(greenLed, GPIO.LOW)
#         else:
#             GPIO.output(redLed, GPIO.LOW)
#             GPIO.output(yellowLed, GPIO.LOW)
#             GPIO.output(greenLed, GPIO.HIGH)

# except KeyboardInterrupt:
#     print("Measurement Stopped by user")
#     GPIO.cleanup()
