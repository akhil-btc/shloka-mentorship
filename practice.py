class Adder:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self, a, b):
        return a + b

adder = Adder(3, 5)
print(adder.add(3, 5))