from machine import Pin
import time
led1 = Pin(12, Pin.OUT)
led2 = Pin(13, Pin.OUT)
led3 = Pin(18, Pin.OUT)
led4 = Pin(19, Pin.OUT)

led1.value(1)
led2.value(1)
led3.value(1)
led4.value(1)

time.sleep(2)

led1.value(0)
led2.value(0)
led3.value(0)
led4.value(0)
