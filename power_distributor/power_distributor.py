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

    # TODO: fix bug when zero pips in a system being drained

    def add_sys_pip(self):
        print("add sys")
        new_sys_power = min(self.sys_power + 2, 8)
        new_eng_power = max(self.eng_power - 1, 0)
        new_wep_power = max(self.wep_power - 1, 0)

        self.set_power(new_sys_power, new_eng_power, new_wep_power)

    def add_eng_pip(self):
        print("add eng")
        new_eng_power = min(self.eng_power + 2, 8)
        new_sys_power = max(self.sys_power - 1, 0)
        new_wep_power = max(self.wep_power - 1, 0)

        self.set_power(new_sys_power, new_eng_power, new_wep_power)


    def add_wep_pip(self):
        print("add wep")
        new_wep_power = min(self.wep_power + 2, 8)
        new_sys_power = max(self.sys_power - 1, 0)
        new_eng_power = max(self.eng_power - 1, 0)

        self.set_power(new_sys_power, new_eng_power, new_wep_power)
