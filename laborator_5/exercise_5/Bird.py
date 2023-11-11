from Animal import Animal


class Bird(Animal):
    def __init__(self, name, environment, legs, can_fly=True):
        super().__init__(name, environment, legs)
        self.can_fly = can_fly

    def show_information(self):
        super().show_information()
        print(f"Can fly: {self.can_fly}")

    def build_nest(self):
        print(f"{self.name} is building a nest.")
