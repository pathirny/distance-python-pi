import gpiozero
import time
led = gpiozero.LED(17)
led.on()
time.sleep(1)
led.off()
time.sleep(1)
led.on()
time.sleep(1)
led.off()