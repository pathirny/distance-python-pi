from gpiozero import LED
import time

blue = LED(17)
red = LED(27)
yellow = LED(22)

for x in range(10):
    blue.on()
    time.sleep(0.1)
    blue.off()
    time.sleep(0.1)
    red.on()
    time.sleep(0.1)
    red.off()
    time.sleep(0.1)
    yellow.on()
    time.sleep(0.1)
    yellow.off()
    time.sleep(0.1)
