from abc import ABC, abstractmethod

class BaseReverser(ABC):
    @abstractmethod
    def reverse_number(self):
        pass

class NumberReverser(BaseReverser):
    def __init__(self, x):
        self.x = x

    def reverse_number(self):
        # Преобразуем число в строку и проверяем знак
        sign = -1 if self.x < 0 else 1
        reversed_str = str(abs(self.x))[::-1]  # Реверсируем строку без знака
        reversed_num = int(reversed_str) * sign  # Применяем знак и конвертируем обратно в int
        return reversed_num

    def __str__(self):
        return str(self.reverse_number())

if __name__ == "__main__":
    x = int(input("Введите целое число: "))
    reverser = NumberReverser(x)
    print(reverser)  # Выводим результат, используя дандер метод __str__