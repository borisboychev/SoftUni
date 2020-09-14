from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        power_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(power_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        heavy_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int,
                                  memory_consumption: int):
        if hardware_name not in [x.name for x in System._hardware]:
            return "Hardware does not exist"

        express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware = [h for h in System._hardware if h.name == hardware_name][0]
        try:
            hardware.install(express_software)
            System._software.append(express_software)
        except Exception as e:
            return str(e)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int,
                                memory_consumption: int):
        if hardware_name not in [x.name for x in System._hardware]:
            return "Hardware does not exist"

        light_software = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware = [h for h in System._hardware if h.name == hardware_name][0]
        try:
            hardware.install(light_software)
            System._software.append(light_software)
        except Exception as e:
            return str(e)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        if hardware_name in [h.name for h in System._hardware] and software_name in [s.name for s in System._software]:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = [s for s in System._software if s.name == software_name][0]
            hardware.uninstall(software)
        else:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        result = ["System Analysis",
                  f"Hardware Components: {len(System._hardware)}",
                  f"Software Components: {len(System._software)}",
                  f"Total Operational Memory: {sum([s.memory_consumption for s in System._software])} / {sum([h.memory for h in System._hardware])}",
                  f"Total Capacity Taken: {sum([s.capacity_consumption for s in System._software])} / {sum([h.capacity for h in System._hardware])}"]

        return "\n".join(result)

    @staticmethod
    def system_split():
        result = ""
        for component in System._hardware:
            result += str(component)
        return result


#
# System.register_power_hardware("HDD", 200, 200)
# System.register_heavy_hardware("SSD", 400, 400)
# print(System.analyze())
# System.register_light_software("HDD", "Test", 0, 10)
# print(System.register_express_software("HDD", "Test2", 100, 100))
# System.register_express_software("HDD", "Test3", 50, 100)
# System.register_light_software("SSD", "Windows", 20, 50)
# System.register_express_software("SSD", "Linux", 50, 100)
# System.register_light_software("SSD", "Unix", 20, 50)
# print(System.analyze())
# System.release_software_component("SSD", "Linux")
# print(System.system_split())

