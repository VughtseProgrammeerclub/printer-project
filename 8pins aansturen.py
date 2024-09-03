#from gpiozero import LED
from machine import Pin
import time

# GPIO0 is fysiek pin 1
# GPIO1 is fysiek pin 2
t = 18,5

nr1 = Pin(0, Pin.OUT)

while True:
    nr1.on()
    time.sleep_us(1000)
    nr1.off()
    time.sleep_us(15000)