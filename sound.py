
from machine import Pin,ADC
import time

sens = ADC(Pin(4))

sens.atten(ADC.ATTN_11DB)

while True:
    value_s = sens.read()
    print(value_s)
    time.sleep(0.5)
