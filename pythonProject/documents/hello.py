# Родительский класс
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def move(self):
        return f"The {self.model} is moving."

    def stop(self):
        return f"The {self.model} has stopped."

# Наследник 1: Машина
class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors

    def open_doors(self):
        return f"Opening {self.doors} doors of the car."

# Наследник 2: Велосипед
class Bike(Vehicle):
    def __init__(self, brand, model, year, bike_type):
        super().__init__(brand, model, year)
        self.bike_type = bike_type

    def ring_bell(self):
        return f"Ringing the bell of the {self.bike_type} bike."

# Пример использования классов
car = Car("Toyota", "Corolla", 2020, 4)
bike = Bike("Giant", "Escape 3", 2021, "mountain")

print(car.move())  # Вывод: The Corolla is moving.
print(car.open_doors())  # Вывод: Opening 4 doors of the car.
print(bike.move())  # Вывод: The Escape 3 is moving.
print(bike.ring_bell())  # Вывод: Ringing the bell of the mountain bike.