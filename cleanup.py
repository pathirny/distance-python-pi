import RPi.GPIO as GPIO

greenLed = 23
yellowLed = 22
redLed= 27

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# gpio set up
GPIO.setup(redLed, GPIO.OUT)
GPIO.setup(yellowLed, GPIO.OUT)
GPIO.setup(greenLed, GPIO.OUT)

GPIO.output(yellowLed, GPIO.LOW)