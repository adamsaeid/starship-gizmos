from machine import Pin
from picozero import Button

from power_indicators import PowerIndicators
from power_distributor import PowerDistributor

ENGINE_BUTTON_PIN = 19
WEP_BUTTON_PIN = 17
SYS_BUTTON_PIN = 20
RESET_BUTTON_PIN = 16

DATA_PIN=13
CLOCK_PIN=14
LATCH_PIN=15

engine_button = Button(ENGINE_BUTTON_PIN)
wep_button = Button(WEP_BUTTON_PIN)
sys_button = Button(SYS_BUTTON_PIN)
reset_button = Button(RESET_BUTTON_PIN)

pins = { 
    'data': Pin(DATA_PIN, Pin.OUT),
    'clock': Pin(CLOCK_PIN, Pin.OUT),
    'latch': Pin(LATCH_PIN, Pin.OUT),
}

power_indicators = PowerIndicators(0, 0, 0,pins)
power_distributor = PowerDistributor(4,4,4,power_indicators)

wep_button.when_pressed = power_distributor.add_wep_pip
engine_button.when_pressed = power_distributor.add_eng_pip
sys_button.when_pressed = power_distributor.add_sys_pip
reset_button.when_pressed = power_distributor.reset_power

