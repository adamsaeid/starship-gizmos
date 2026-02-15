from machine import Pin
from picozero import Button

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

weapon_indicator = {
    "power": 4,
}

engine_indicator = {
    "power": 4,
}

sys_indicator = {
    "power": 4
}

power_distributor = PowerDistributor(4,4,4,pins)

def increment_power(indicator, other_indicators):
    indicator["power"] = min(indicator["power"] + 2, 8)
   
    for other_indicator in other_indicators:
        other_indicator["power"] = max(other_indicator["power"] - 1, 0)

def display_power():
    sys_power = sys_indicator.get('power')
    eng_power = engine_indicator.get('power')
    wep_power = weapon_indicator.get('power')

    power_distributor.set_power(sys_power, eng_power, wep_power)

def handle_press(indicator, other_indicators):
    increment_power(indicator, other_indicators)
    display_power()

def handle_weapon_press():
    handle_press(weapon_indicator, [sys_indicator, engine_indicator])

def handle_engine_press():
    handle_press(engine_indicator, [sys_indicator, weapon_indicator])
   
def handle_sys_press():
    handle_press(sys_indicator, [engine_indicator, weapon_indicator])

weapon_button.when_pressed = handle_weapon_press
engine_button.when_pressed = handle_engine_press
sys_button.when_pressed = handle_sys_press

