from project.technology.technology import Technology

class Laptop(Technology):
    def __init__(self, memory, memory_taken):
        Technology.__init__(self,memory, memory_taken)

    def install_software(self, software, software_memory):
        try:
            memory_left = self.get_capacity(self.memory, self.memory_taken + software_memory)
            self.memory_taken += software_memory
            return memory_left
        except Exception as e:
            return f"You don't have enough space for {software}!"

# laptop = Laptop(1000, 20)
# print(laptop.install_software('rust' , 5000))
# print(laptop.install_software('spotify' , 500))
