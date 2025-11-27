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
    def __str__(self) -> str:
        """Строковое представление числа"""
        pass

    @abstractmethod
    def __repr__(self) -> str:
        """Формальное строковое представление объекта"""
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

    def __init__(self, digits: Optional[List[int]] = None) -> None:
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

    def __str__(self) -> str:
        """Строковое представление в виде десятичного числа"""
        return str(self._to_int())

    def __repr__(self) -> str:
        """Формальное представление в виде массива цифр"""
        return f"Decimal({self.digits})"

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
        result = self._to_int() // other._to_int()
        return Decimal._from_int(result)


class Binary(Integer):
    """Класс для двоичных чисел"""

    def __init__(self, digits: Optional[List[int]] = None) -> None:
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

    def __str__(self) -> str:
        """Строковое представление в виде двоичного числа"""
        return "".join(map(str, self.digits))

    def __repr__(self) -> str:
        """Формальное представление в виде массива битов"""
        return f"Binary({self.digits})"

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
        result = self._to_int() // other._to_int()
        return Binary._from_int(result)


class Reader:
    @staticmethod
    def read_decimal() -> Decimal:
        """Чтение десятичного числа с клавиатуры"""
        try:
            num_str = input("Введите десятичное число: ")
            num = int(num_str)
            return Decimal._from_int(num)
        except ValueError:
            raise ValueError("Некорректный ввод десятичного числа")

    @staticmethod
    def read_binary() -> Binary:
        """Чтение двоичного числа с клавиатуры"""
        try:
            bin_str = input("Введите двоичное число: ")
            if not all(bit in "01" for bit in bin_str):
                raise ValueError()
            return Binary([int(bit) for bit in bin_str])
        except ValueError:
            raise ValueError("Некорректный ввод двоичного числа")


def demonstrate_output(number_obj: Integer) -> None:
    print("Виртуальный вызов:")
    print(f"Строковое представление: {number_obj}")
    print(f"Формальное представление: {repr(number_obj)}")


if __name__ == "__main__":
    dec1 = Decimal([1, 2, 3])
    print(f"dec1: {dec1} (repr: {repr(dec1)})")

    dec2 = Decimal([4, 5])
    print(f"dec2: {dec2} (repr: {repr(dec2)})")

    result_add = dec1.add(dec2)
    print(f"123 + 45 = {result_add}")

    result_sub = dec1.subtract(dec2)
    print(f"123 - 45 = {result_sub}")

    result_mul = dec1.multiply(dec2)
    print(f"123 * 45 = {result_mul}")

    result_div = dec1.divide(dec2)
    print(f"123 // 45 = {result_div}")

    bin1 = Binary([1, 0, 1, 0])
    print(f"bin1: {bin1} (repr: {repr(bin1)})")

    bin2 = Binary([1, 1, 0])
    print(f"bin2: {bin2} (repr: {repr(bin2)})")

    result_add_bin = bin1.add(bin2)
    print(f"1010 + 110 = {result_add_bin}")

    result_sub_bin = bin1.subtract(bin2)
    print(f"1010 - 110 = {result_sub_bin}")

    result_mul_bin = bin1.multiply(bin2)
    print(f"1010 * 110 = {result_mul_bin}")

    result_div_bin = bin1.divide(bin2)
    print(f"1010 // 110 = {result_div_bin}")

    demonstrate_output(dec1)
    demonstrate_output(bin1)

    try:
        dec_input = Reader.read_decimal()
        demonstrate_output(dec_input)

        bin_input = Reader.read_binary()
        demonstrate_output(bin_input)
    except Exception as e:
        print(f"Ошибка ввода: {e}")
