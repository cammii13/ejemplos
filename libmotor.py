from machine import Pin
import time
# Motor 1
m1_pin_a = Pin(12, Pin.OUT)
m1_pin_b = Pin(13, Pin.OUT)
# Motor 2
m2_pin_a = Pin(18, Pin.OUT)
m2_pin_b = Pin(19, Pin.OUT)

def carro_adelante():
    m1_pin_a.on()
    m1_pin_b.off()
    m2_pin_a.on()
    m2_pin_b.off()

def carro_atras():
    m1_pin_a.off()
    m1_pin_b.on()
    m2_pin_a.off()
    m2_pin_b.on()

def carro_izquierda():
    m1_pin_a.off()
    m1_pin_b.on()
    m2_pin_a.on()
    m2_pin_b.off()
    
def carro_derecha():
    m1_pin_a.on()
    m1_pin_b.off()
    m2_pin_a.off()
    m2_pin_b.on()

def carro_parar():
    m1_pin_a.off()
    m1_pin_b.off()
    m2_pin_a.off()
    m2_pin_b.off()