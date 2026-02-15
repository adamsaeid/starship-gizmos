from machine import Pin
from picozero import Button

from power_indicators import PowerIndicators
from power_distributor import PowerDistributor

engine_button = Button(19)
weapon_button = Button(17)
sys_button = Button(20)

dataPIN=Pin(13, Pin.OUT)
clockPIN=Pin(14, Pin.OUT)
latchPIN=Pin(15, Pin.OUT)

pins = { 
    'data': dataPIN,
    'latch': latchPIN,
    'clock': clockPIN
}

power_indicators = PowerIndicators(0, 0, 0,pins)
power_distributor = PowerDistributor(4,4,4,power_indicators)

weapon_button.when_pressed = power_distributor.add_wep_pip
engine_button.when_pressed = power_distributor.add_eng_pip
sys_button.when_pressed = power_distributor.add_sys_pip

