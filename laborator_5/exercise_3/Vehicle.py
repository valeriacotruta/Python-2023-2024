class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def show_information(self):
        print(f"Make: {self.make}, model: {self.model}, year: {self.year}")
