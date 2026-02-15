from machine import Pin
import utime
import random

from power_indicators import PowerIndicators

dataPIN = 13
latchPIN = 15
clockPIN = 14

dataPIN=Pin(dataPIN, Pin.OUT)
latchPIN=Pin(latchPIN, Pin.OUT)
clockPIN=Pin(clockPIN, Pin.OUT)

pins = { 'data': dataPIN, 'latch': latchPIN, 'clock': clockPIN }


power_indicators = PowerIndicators(2, 2, 2, pins)

def sleep():
    sleep_time = random.uniform(0.3, 1.0)
    utime.sleep(sleep_time)

while True:
    sleep()
    power_indicators.set_power(2, 2, 2)
    sleep()
    power_indicators.set_power(4, 1, 1)
    sleep()
    power_indicators.set_power(6, 0, 0)
    sleep()
    power_indicators.set_power(4, 2, 0)
    sleep()
    power_indicators.set_power(3, 1, 2)
    sleep()
    power_indicators.set_power(2, 3, 1)
    sleep()
    power_indicators.set_power(1, 5, 0)
    sleep()
    power_indicators.set_power(2, 3, 1)
    sleep()
    power_indicators.set_power(1, 2, 3)
    sleep()
    power_indicators.set_power(1, 1, 4)
    sleep()
    power_indicators.set_power(1, 0, 5)
