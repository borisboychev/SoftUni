class Glass:

    def __init__(self):
        self.content = 0
        self.capacity = 250

    def fill(self, ml: int):
        if self.content >= self.capacity or self.content + ml > self.capacity:
            return f"Cannot add {ml} ml"
        self.content += ml
        return f"Glass filled with {ml} ml"

    def empty(self):
        self.content = 0
        return f"Glass is now empty"

    def info(self):
        return f"{abs(self.content - self.capacity)} ml left"


glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())
