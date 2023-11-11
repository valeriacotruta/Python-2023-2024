from Vehicle import Vehicle


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, fuel):
        super().__init__(make, model, year)
        self.fuel = fuel

    def calculate_mileage(self, distance):
        return print(f"Mileage for {distance} km with {self.fuel} liters :{distance / self.fuel}.")
