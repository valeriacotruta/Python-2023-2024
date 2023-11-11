from Vehicle import Vehicle


class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity

    def get_towing_capacity(self):
        return print(f"Towing capacity:{self.towing_capacity}.")
