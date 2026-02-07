from picozero import LED, Button

engine_button = Button(17)
weapon_button = Button(16)
sys_button = Button(22)

power_thresholds = [
    1,
    3,
    5,
    7
]

weapon_leds = [
    LED(15),
    LED(14),
    LED(13),
    LED(12),
]

engine_leds = [
    LED(11),
    LED(10),
    LED(9),
    LED(8),
]

sys_leds = [
    LED(18),
    LED(19),
    LED(20),
    LED(21),
]

weapon_indicator = {
    "leds": weapon_leds,
    "power": 4,
}

engine_indicator = {
    "leds": engine_leds,
    "power": 4,
}

sys_indicator = {
    "leds": sys_leds,
    "power": 4
}

def increment_power(indicator, other_indicators):
    indicator["power"] = min(indicator["power"] + 2, 8)
   
    for other_indicator in other_indicators:
        other_indicator["power"] = max(other_indicator["power"] - 1, 0)

def display_power(indicator):
    system_leds = indicator["leds"]
    system_power = indicator["power"]
   
    for index, led in enumerate(system_leds):
        if system_power > power_thresholds[index]:
            led.on()
            led.brightness = 1
        elif system_power == power_thresholds[index]:
            led.on()
            led.brightness = 0.1
        else:
            led.off()

def handle_press(indicator, other_indicators):
    increment_power(indicator, other_indicators)
    display_power(indicator)
   
    for other_indicator in other_indicators:
        display_power(other_indicator)
       
    print(indicator["power"])

def handle_weapon_press():
    handle_press(weapon_indicator, [sys_indicator, engine_indicator])

def handle_engine_press():
    handle_press(engine_indicator, [sys_indicator, weapon_indicator])
   
def handle_sys_press():
    handle_press(sys_indicator, [engine_indicator, weapon_indicator])

weapon_button.when_pressed = handle_weapon_press
engine_button.when_pressed = handle_engine_press
sys_button.when_pressed = handle_sys_press

display_power(weapon_indicator)
display_power(engine_indicator)
display_power(sys_indicator)