class PowerIndicators:
    def __init__(self, sys_power, eng_power, wep_power, pins):
        self.data_pin = pins.get('data')
        self.latch_pin = pins.get('latch')
        self.clock_pin = pins.get('clock')

        self.set_power(sys_power, eng_power, wep_power)

    def set_power(self, sys_power, eng_power, wep_power):
        self.sys_power = sys_power
        self.eng_power = eng_power
        self.wep_power = wep_power

        self.display_power()


    def subsystem_power_string(self, subsystem_power):
        power_string = "00000000"

        for i in range(subsystem_power):
            power_string = power_string[1:] + str(1)

        return power_string
    
    def shift_update(self, power_string):
        self.latch_pin.value(0)
  
        for i in range(len(power_string)):
            self.clock_pin.value(0)
            self.data_pin.value(int(power_string[i]))
            self.clock_pin.value(1)

        self.latch_pin.value(1)
        self.latch_pin.value(0)

    def display_power(self):
        power_string = self.subsystem_power_string(self.sys_power) + self.subsystem_power_string(self.eng_power) + self.subsystem_power_string(self.wep_power)
        self.shift_update(power_string)

