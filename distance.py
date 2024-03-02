import gpiozero
import time
led = gpiozero.LED(17)


for x in range(10):
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)
    