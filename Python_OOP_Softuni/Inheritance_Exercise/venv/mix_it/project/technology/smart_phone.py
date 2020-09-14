from project.technology.technology import Technology

class SmartPhone(Technology):
    def __init__(self, memory, memory_taken):
        Technology.__init__(self, memory, memory_taken)

    def install_apps(self, app, app_memory):
        try:
            memory_left = self.get_capacity(self.memory, self.memory_taken + app_memory)
            self.memory_taken += app_memory
            return memory_left
        except Exception as e:
            return f"You don't have enough space for {app}!"


# phone = SmartPhone(1000, 20)
# print(phone.install_apps('rust+', 1024))
# print(phone.install_apps('spotify', 960))