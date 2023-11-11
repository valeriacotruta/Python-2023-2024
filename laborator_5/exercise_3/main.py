# Create a base class Vehicle with attributes like make, model, and year,
# and then create subclasses for specific types of vehicles like Car, Motorcycle, and Truck.
# Add methods to calculate mileage or towing capacity based on the vehicle type.
import exercise_3 as ex_3

my_car = ex_3.Car(make="Toyota", model="Camry", year=2022, fuel=30)
my_car.show_information()
my_car.calculate_mileage(distance=300)

my_motorcycle = ex_3.Motorcycle(make="Harley-Davidson", model="Sportster", year=2022, fuel=30)
my_motorcycle.show_information()
my_motorcycle.calculate_mileage(distance=300)

my_truck = ex_3.Truck(make="Ford", model="F-150", year=2022, towing_capacity=8000)
my_truck.show_information()
my_truck.get_towing_capacity()
