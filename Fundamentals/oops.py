class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand # private
        self.__model = model # private
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    # no need for self reference in static method -> only accessed by class not obj
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    # attr cannot change, just viewed
    @property
    def model(self):
        return self.__model
    

# inheritance
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"


my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

# gives boolean answer
print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElectricCar))

# print(my_tesla.__brand)
# print(my_tesla.fuel_type())

# my_car = Car("Tata", "Safari")
# my_car.model = "City"
# Car("Tata", "Nexon")

# print(my_car.general_description())
# # access as property ".model" instead of method ".model()"
# print(my_car.model)


# my_car = Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_new_car = Car("Tata", "Safari")
# print(my_new_car.model)

# print(Car.total_car)


class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "This is engine"

# multi inheritance
class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())