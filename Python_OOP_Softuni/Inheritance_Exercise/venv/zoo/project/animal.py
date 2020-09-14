class Animal:

    def __init__(self, name):
        self.name = name

    def __getattr__(self, item):
        return self.name