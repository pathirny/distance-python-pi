import RPi.GPIO as GPIO
import time

# Set the GPIO mode and warnings
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins for LEDs and ultrasonic sensor
GREEN = 23
YELLOW = 22
RED = 27
PIN_TRIGGER = 4
PIN_ECHO = 17

# Set up GPIO pins
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(YELLOW, GPIO.OUT)
GPIO.setup(PIN_TRIGGER, GPIO.OUT)
GPIO.setup(PIN_ECHO, GPIO.IN)
GPIO.setup(GREEN, GPIO.OUT)

def green_light():
    GPIO.output(GREEN, GPIO.HIGH)
    GPIO.output(YELLOW, GPIO.LOW)
    GPIO.output(RED, GPIO.LOW)

def yellow_light():
    GPIO.output(GREEN, GPIO.LOW)
    GPIO.output(YELLOW, GPIO.HIGH)
    GPIO.output(RED, GPIO.LOW)

def red_light():
    GPIO.output(GREEN, GPIO.LOW)
    GPIO.output(YELLOW, GPIO.LOW)
    GPIO.output(RED, GPIO.HIGH) 

def get_distance():
    GPIO.output(PIN_TRIGGER, True)  # Set trigger to HIGH
    time.sleep(0.0001)
    GPIO.output(PIN_TRIGGER, False)  # Set trigger to LOW

    startTime = time.time()
    endTime = time.time()

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
    print(f"Distance: {distance}")
#     if distance >= 9:
#         green_light()
#     elif distance < 9 and distance > 7:
#         yellow_light()
#     elif distance <= 6:
#         red_light()


# try:
#     while True:
#         dist = distance()
#         print(f"Measured distance = {dist} cm")
#         time.sleep(1)

#         if dist < 5:
#             GPIO.output(RED, GPIO.HIGH)
#             GPIO.output(YELLOW, GPIO.LOW)
#             GPIO.output(GREEN, GPIO.LOW)
#         elif 5 <= dist < 20:
#             GPIO.output(RED, GPIO.LOW)
#             GPIO.output(YELLOW, GPIO.HIGH)
#             GPIO.output(GREEN, GPIO.LOW)
#         else:
#             GPIO.output(RED, GPIO.LOW)
#             GPIO.output(YELLOW, GPIO.LOW)
#             GPIO.output(GREEN, GPIO.HIGH)

# except KeyboardInterrupt:
#     print("Measurement Stopped by user")
#     GPIO.cleanup()
