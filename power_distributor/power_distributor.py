from power_indicators import PowerIndicators

class PowerDistributor:
    def __init__(self, sys_power, eng_power, wep_power, power_indicators):
        self.power_indicators = power_indicators
        self.set_power(sys_power, eng_power, wep_power)

    def set_power(self, sys_power, eng_power, wep_power):
        self.sys_power = sys_power
        self.eng_power = eng_power
        self.wep_power = wep_power

        self.power_indicators.set_power(sys_power, eng_power, wep_power)

    # TODO: fix bug when zero pips in a system being drained

    def add_sys_pip(self):
        new_sys_power = min(self.sys_power + 2, 8)
        new_eng_power = max(self.eng_power - 1, 0)
        new_wep_power = max(self.wep_power - 1, 0)

        self.set_power(new_sys_power, new_eng_power, new_wep_power)

    def add_eng_pip(self):
        new_eng_power = min(self.eng_power + 2, 8)
        new_sys_power = max(self.sys_power - 1, 0)
        new_wep_power = max(self.wep_power - 1, 0)

        self.set_power(new_sys_power, new_eng_power, new_wep_power)


    def add_wep_pip(self):
        new_wep_power = min(self.wep_power + 2, 8)
        new_sys_power = max(self.sys_power - 1, 0)
        new_eng_power = max(self.eng_power - 1, 0)

        self.set_power(new_sys_power, new_eng_power, new_wep_power)

    def reset_power(self):
        self.set_power(4,4,4)
