from power_indicators import PowerIndicators

class PowerDistributor:
    def __init__(self, sys_power, eng_power, wep_power, pins):
        self.power_indicators = PowerIndicators(sys_power, eng_power, wep_power, pins)
        self.set_power(sys_power, eng_power, wep_power)

    def set_power(self, sys_power, eng_power, wep_power):
        self.sys_power = sys_power
        self.eng_power = eng_power
        self.wep_power = wep_power

        self.power_indicators.set_power(sys_power, eng_power, wep_power)
