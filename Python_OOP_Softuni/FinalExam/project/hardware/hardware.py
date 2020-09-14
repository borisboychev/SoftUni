from project.software.software import Software


class Hardware:
    def __init__(self, name, type, capacity, memory):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        if value == "Heavy":
            self._type = value
        if value == "Power":
            self._type = value

    def has_memory(self, software):
        memory = sum([s.memory_consumption for s in self.software_components]) + software.memory_consumption
        return memory <= self.memory

    def has_space(self, software):
        capacity = sum([s.capacity_consumption for s in self.software_components]) + software.capacity_consumption
        return capacity <= self.capacity

    def install(self, software: Software):
        if self.has_space(software) and self.has_memory(software):
            self.software_components.append(software)
        else:
            raise Exception("Software cannot be installed")

    def uninstall(self, software: Software):
        self.software_components.remove(software)

    def __str__(self):
        result = [f"Hardware Component - {self.name}",
                  f"Express Software Components: {len([x for x in self.software_components if x.type == 'Express'])}",
                  f"Light Software Components: {len([x for x in self.software_components if x.type == 'Light'])}",
                  f"Memory Usage: {sum([s.memory_consumption for s in self.software_components])} / {self.memory}",
                  f"Capacity Usage: {sum([s.capacity_consumption for s in self.software_components])} / {self.capacity}",
                  f"Type: {self.type}",
                  f"Software Components: {', '.join([str(s) for s in self.software_components]) if self.software_components else 'None'}"]

        return "\n".join(result)

