from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    def __init__(self, name, capacity, memory):
        Hardware.__init__(self,name, 'Power', int(capacity*0.25), int(memory*1.75))
