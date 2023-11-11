from Animal import Animal

class Mammal(Animal):
    def __init__(self, name, environment, legs, fur_color):
        super().__init__(name, environment, legs)
        self.fur_color = fur_color

    def show_information(self):
        super().show_information()
        print(f"Fur Color: {self.fur_color}")
