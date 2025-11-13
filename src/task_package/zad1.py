import math
from typing import Union


class Number:
    """Базовый класс для чисел типа float"""

    def __init__(self, value: Union[float, int] = 0.0) -> None:
        self._value = float(value)

    def add(self, other: Union["Number", float, int]) -> "Number":
        """Сложение"""
        if isinstance(other, Number):
            return Number(self._value + other._value)
        return Number(self._value + float(other))

    def divide(self, other: Union["Number", float, int]) -> "Number":
        """Деление"""
        if isinstance(other, Number):
            if other._value == 0:
                raise ValueError("Деление на ноль невозможно")
            return Number(self._value / other._value)
        other_val = float(other)
        if other_val == 0:
            raise ValueError("Деление на ноль невозможно")
        return Number(self._value / other_val)

    def __str__(self) -> str:
        return str(self._value)

    def __repr__(self) -> str:
        return f"Number({self._value})"


class Real(Number):
    """Производный класс для возведения
    в производную степень и нахождения логарифма"""

    def power(self, exponent: Union["Real", float, int]) -> "Real":
        """Возведение в произвольную степень"""
        if isinstance(exponent, Real):
            exp_val = exponent._value
        else:
            exp_val = float(exponent)
        return Real(self._value**exp_val)

    def logarithm(self, base: Union["Real", float, int, None] = None) -> "Real":
        """Вычисление логарифма числа"""
        if base is None:
            if self._value <= 0:
                raise ValueError("Логарифм определен только для положительных чисел")
            return Real(math.log(self._value))
        else:
            if isinstance(base, Real):
                base_val = base._value
            else:
                base_val = float(base)

            if self._value <= 0 or base_val <= 0 or base_val == 1:
                raise ValueError("Некорректные значения для логарифма")

            return Real(math.log(self._value, base_val))

    def __repr__(self) -> str:
        return f"Real({self._value})"


if __name__ == "__main__":
    num1 = Number(10.5)
    num2 = Number(2.5)

    print(f"num1 = {num1}")
    print(f"num2 = {num2}")
    print(f"Сложение: {num1.add(num2)}")
    print(f"Деление: {num1.divide(num2)}")

    real1 = Real(8.0)
    real2 = Real(2.0)

    print(f"real1 = {real1}")
    print(f"real2 = {real2}")
    print(f"Возведение в степень: {real1.power(real2)}")
    print(f"Возведение в степень 0.5 (квадратный корень): {real1.power(0.5)}")
    print(f"Логарифм по основанию 2: {real1.logarithm(2)}")

    print(f"real1 + 5 = {real1.add(5)}")
    print(f"real1 в степени 3 = {real1.power(3)}")
