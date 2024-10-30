from machine import Pin, Timer
import time

led = machine.Pin("LED", machine.Pin.OUT)
timer = Timer()
knoprood = Pin(13, Pin.IN)
knopwit = Pin(14, Pin.IN)
knopblauw = Pin(15, Pin.IN)

while True:
#    print("rood", knoprood.value())
#    print("wit", knopwit.value())
#    print("blauw", knopblauw.value())
    
    if knoprood.value()==1:
        led.on()
    elif knopblauw.value()==1:
        led.off()
    elif knopwit.value()==1:
        led.toggle()
    time.sleep(1)
    
