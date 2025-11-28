import machine
import time
import neopixel

PIN = 4
NUM_PIX = 3
np = neopixel.NeoPixel(machine.Pin(PIN), NUM_PIX)
np[0] = (255, 0, 242)
np[1] = (255, 125, 253)
np[2] = (255, 179, 252)
np.write()