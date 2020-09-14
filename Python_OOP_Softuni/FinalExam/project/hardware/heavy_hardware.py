from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    def __init__(self, name, capacity, memory):
        Hardware.__init__(self, name, "Heavy", int(capacity*2), int(memory * 0.75))
