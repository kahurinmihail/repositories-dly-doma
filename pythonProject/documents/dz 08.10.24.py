from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self,model,year,max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    # Абстрактный метод для запуска двигателя
    @abstractmethod
    def start_engine(self):
        pass

    # Абстрактный метод для движения вперед
    @abstractmethod
    def move_forward(self):
        pass

    # Абстрактный метод для движения назад
    @abstractmethod
    def move_backward(self):
        pass

class Car(Vehicle):
    def __init__(self, model, year, max_speed,Shinie):
        super().__init__(model,year,max_speed)
        self.Shinie = Shinie

    def start_engine(self):
        return "Двигатель заведен."

    def move_forward(self):
        return "Машина едет вперед."

    def move_backward(self):
        return "Машина едет назад."

class Bike(Vehicle):
    def __init__(self, model, year, max_speed, kolichestvo_passajirov):
        super().__init__(model,year,max_speed)
        self.kolichestvo_passajirov = kolichestvo_passajirov

    def start_engine(self):
        return "Двигатель заведен"

    def move_forward(self):
        return "Мотоцикл едет вперед."

    def move_backward(self):
        return "Мотоцикл едет назад."

car = Car("Toyota", "2024", 200, "Meshlenn")
print(car.model)
print(car.start_engine())   # Вывод: Car engine started.
print(car.move_forward())   # Вывод: Car is moving forward.
print(car.move_backward())  # Вывод: Car is moving backward.

bike = Bike("Yamaha", "2022", 250, 2)
print(bike.model)
print(bike.start_engine())   # Вывод: Bike doesn't have an engine, but we are ready to pedal!
print(bike.move_forward())   # Вывод: Bike is moving forward.
print(bike.move_backward())  # Вывод: Bike is moving backward.

