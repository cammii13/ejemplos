from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

i2c= I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)
print("Dispositivos I2C encontrados:", i2c.scan())
ancho = 128
alto = 64
oled = SSD1306_I2C(ancho, alto, i2c)

oled.fill(0)
oled.text("Extrañamos a Johanán", 0, 0)
oled.text(":3", 0, 16)
oled.show()