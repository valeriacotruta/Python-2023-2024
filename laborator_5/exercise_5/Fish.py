from Animal import Animal


class Fish(Animal):
    def __init__(self, name, environment, legs, can_swim=True):
        super().__init__(name, environment, legs)
        self.can_swim = can_swim

    def show_information(self):
        super().show_information()
        print(f"Can swim: {self.can_swim}")

