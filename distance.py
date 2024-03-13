import RPi.GPIO as GPIO
import time

# Set the GPIO mode and warnings
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins for LEDs and ultrasonic sensor
greenLed = 23
yellowLed = 22
redLed = 27
PIN_TRIGGER = 4
PIN_ECHO = 17

# Set up GPIO pins
GPIO.setup(redLed, GPIO.OUT)
GPIO.setup(yellowLed, GPIO.OUT)
GPIO.setup(PIN_TRIGGER, GPIO.OUT)
GPIO.setup(PIN_ECHO, GPIO.IN)
GPIO.setup(greenLed, GPIO.OUT)

def green_light():
    GPIO.output(greenLed, GPIO.HIGH)
    GPIO.output(yellowLed, GPIO.LOW)
    GPIO.output(redLed, GPIO.LOW)

def yellow_light():
    GPIO.output(greenLed, GPIO.LOW)
    GPIO.output(yellowLed, GPIO.HIGH)
    GPIO.output(redLed, GPIO.LOW)

def red_light():
    GPIO.output(greenLed, GPIO.LOW)
    GPIO.output(yellowLed, GPIO.LOW)
    GPIO.output(redLed, GPIO.HIGH) 

def get_distance():
    GPIO.output(PIN_TRIGGER, True)  # Set trigger to HIGH
    time.sleep(0.0001)
    GPIO.output(PIN_TRIGGER, False)  # Set trigger to LOW

    # Wait for the echo pulse
    while GPIO.input(PIN_ECHO) == False:
        startTime = time.time()
    while GPIO.input(PIN_ECHO) == True:
        endTime = time.time()

    duration = endTime - startTime
    distance = duration / 0.000058

    return distance

while True: 
    distance = get_distance()
    time.sleep(0.05)

    if distance >= 9:
        green_light()
    elif distance < 9 and distance > 7:
        yellow_light()
    elif distance <= 6:
        red_light()


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
