from abc import ABC, abstractmethod
from typing import List, Optional, TypeVar

T = TypeVar("T", bound="Integer")


class Integer(ABC):
    """Абстрактный базовый класс для целых чисел"""

    def __init__(self, digits: Optional[List[int]] = None) -> None:
        if digits is None:
            digits = [0]
        self.digits = digits

    @abstractmethod
    def input(self) -> None:
        """Абстрактный метод ввода числа"""
        pass

    @abstractmethod
    def output(self) -> None:
        """Абстрактный метод вывода числа"""
        pass

    @abstractmethod
    def add(self: T, other: T) -> T:
        """Абстрактный метод сложения"""
        pass

    @abstractmethod
    def subtract(self: T, other: T) -> T:
        """Абстрактный метод вычитания"""
        pass

    @abstractmethod
    def multiply(self: T, other: T) -> T:
        """Абстрактный метод умножения"""
        pass

    @abstractmethod
    def divide(self: T, other: T) -> T:
        """Абстрактный метод деления"""
        pass


class Decimal(Integer):
    """Класс для десятичных чисел"""

    def __init__(self, digits: Optional[List[int]] = None) -> None:  # Исправлено
        super().__init__(digits)
        self._validate_digits()

    def _validate_digits(self) -> None:
        """Проверка корректности цифр (0-9)"""
        for digit in self.digits:
            if not 0 <= digit <= 9:
                raise ValueError("Цифры должны быть в диапазоне 0-9")

    def _to_int(self) -> int:
        """Преобразование массива цифр в целое число"""
        return int("".join(map(str, self.digits)))

    @classmethod
    def _from_int(cls, num: int) -> "Decimal":
        """Создание объекта из целого числа"""
        if num == 0:
            return cls([0])
        digits: List[int] = []
        n = abs(num)
        while n > 0:
            digits.insert(0, n % 10)
            n //= 10
        return cls(digits)

    def input(self) -> None:
        """Ввод десятичного числа с клавиатуры"""
        try:
            num_str = input("Введите десятичное число: ")
            num = int(num_str)
            new_obj = self._from_int(num)
            self.digits = new_obj.digits
            self._validate_digits()
        except ValueError:
            raise ValueError("Некорректный ввод десятичного числа")

    def output(self) -> None:
        """Вывод десятичного числа"""
        print(f"Десятичное число: {self._to_int()}")
        print(f"Представление в виде массива цифр: {self.digits}")

    def add(self, other: "Decimal") -> "Decimal":
        """Сложение десятичных чисел"""
        if not isinstance(other, Decimal):
            raise TypeError("Можно складывать только десятичные числа")
        result = self._to_int() + other._to_int()
        return Decimal._from_int(result)

    def subtract(self, other: "Decimal") -> "Decimal":
        """Вычитание десятичных чисел"""
        if not isinstance(other, Decimal):
            raise TypeError("Можно вычитать только десятичные числа")
        result = self._to_int() - other._to_int()
        return Decimal._from_int(result)

    def multiply(self, other: "Decimal") -> "Decimal":
        """Умножение десятичных чисел"""
        if not isinstance(other, Decimal):
            raise TypeError("Можно умножать только десятичные числа")
        result = self._to_int() * other._to_int()
        return Decimal._from_int(result)

    def divide(self, other: "Decimal") -> "Decimal":
        """Деление десятичных чисел"""
        if not isinstance(other, Decimal):
            raise TypeError("Можно делить только десятичные числа")
        if other._to_int() == 0:
            raise ValueError("Деление на ноль")
        result = self._to_int() // other._to_int()  # целочисленное деление
        return Decimal._from_int(result)


class Binary(Integer):
    """Класс для двоичных чисел"""

    def __init__(self, digits: Optional[List[int]] = None) -> None:  # Исправлено
        super().__init__(digits)
        self._validate_bits()

    def _validate_bits(self) -> None:
        """Проверка корректности битов (0 или 1)"""
        for bit in self.digits:
            if bit not in (0, 1):
                raise ValueError("Биты должны быть 0 или 1")

    def _to_int(self) -> int:
        """Преобразование массива битов в целое число"""
        return int("".join(map(str, self.digits)), 2)

    @classmethod
    def _from_int(cls, num: int) -> "Binary":
        """Создание объекта из целого числа"""
        if num == 0:
            return cls([0])
        bits: List[int] = []
        n = abs(num)
        while n > 0:
            bits.insert(0, n % 2)
            n //= 2
        return cls(bits)

    def input(self) -> None:
        """Ввод двоичного числа с клавиатуры"""
        try:
            bin_str = input("Введите двоичное число: ")
            # Проверяем, что строка содержит только 0 и 1
            if not all(bit in "01" for bit in bin_str):
                raise ValueError()
            self.digits = [int(bit) for bit in bin_str]
            self._validate_bits()
        except ValueError:
            raise ValueError("Некорректный ввод двоичного числа")

    def output(self) -> None:
        """Вывод двоичного числа"""
        print(f"Двоичное число: {''.join(map(str, self.digits))}")
        print(f"Десятичное значение: {self._to_int()}")
        print(f"Представление в виде массива битов: {self.digits}")

    def add(self, other: "Binary") -> "Binary":
        """Сложение двоичных чисел"""
        if not isinstance(other, Binary):
            raise TypeError("Можно складывать только двоичные числа")
        result = self._to_int() + other._to_int()
        return Binary._from_int(result)

    def subtract(self, other: "Binary") -> "Binary":
        """Вычитание двоичных чисел"""
        if not isinstance(other, Binary):
            raise TypeError("Можно вычитать только двоичные числа")
        result = self._to_int() - other._to_int()
        return Binary._from_int(result)

    def multiply(self, other: "Binary") -> "Binary":
        """Умножение двоичных чисел"""
        if not isinstance(other, Binary):
            raise TypeError("Можно умножать только двоичные числа")
        result = self._to_int() * other._to_int()
        return Binary._from_int(result)

    def divide(self, other: "Binary") -> "Binary":
        """Деление двоичных чисел"""
        if not isinstance(other, Binary):
            raise TypeError("Можно делить только двоичные числа")
        if other._to_int() == 0:
            raise ValueError("Деление на ноль")
        result = self._to_int() // other._to_int()  # целочисленное деление
        return Binary._from_int(result)


def demonstrate_output(number_obj: Integer) -> None:
    """
    Функция для демонстрации виртуального вызова
    Получает параметр базового класса по ссылке
    """
    print("Виртуальный вызов:")
    number_obj.output()


if __name__ == "__main__":
    dec1 = Decimal([1, 2, 3])
    dec1.output()

    dec2 = Decimal([4, 5])
    dec2.output()

    result_add = dec1.add(dec2)
    print("123 + 45 =", end=" ")
    result_add.output()

    result_sub = dec1.subtract(dec2)
    print("123 - 45 =", end=" ")
    result_sub.output()

    result_mul = dec1.multiply(dec2)
    print("123 * 45 =", end=" ")
    result_mul.output()

    result_div = dec1.divide(dec2)
    print("123 // 45 =", end=" ")
    result_div.output()

    bin1 = Binary([1, 0, 1, 0])
    bin1.output()

    bin2 = Binary([1, 1, 0])
    bin2.output()

    result_add_bin = bin1.add(bin2)
    print("1010 + 110 =", end=" ")
    result_add_bin.output()

    result_sub_bin = bin1.subtract(bin2)
    print("1010 - 110 =", end=" ")
    result_sub_bin.output()

    result_mul_bin = bin1.multiply(bin2)
    print("1010 * 110 =", end=" ")
    result_mul_bin.output()

    result_div_bin = bin1.divide(bin2)
    print("1010 // 110 =", end=" ")
    result_div_bin.output()

    demonstrate_output(dec1)
    demonstrate_output(bin1)

    try:
        dec_input = Decimal()
        dec_input.input()
        demonstrate_output(dec_input)

        bin_input = Binary()
        bin_input.input()
        demonstrate_output(bin_input)
    except Exception as e:
        print(f"Ошибка ввода: {e}")
