import math
import os
import sys
from typing import Union

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))


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


class TestNumber:
    """Тесты для базового класса Number"""

    def test_init_default(self):
        """Тест инициализации с значениями по умолчанию"""
        num = Number()
        assert num._value == 0.0

    def test_init_with_value(self):
        """Тест инициализации с заданным значением"""
        num = Number(5.5)
        assert num._value == 5.5

    def test_init_with_int(self):
        """Тест инициализации с целым числом"""
        num = Number(10)
        assert num._value == 10.0

    def test_add_with_number(self):
        """Тест сложения двух Number объектов"""
        num1 = Number(10.5)
        num2 = Number(2.5)
        result = num1.add(num2)
        assert result._value == 13.0

    def test_add_with_float(self):
        """Тест сложения Number с float"""
        num = Number(5.5)
        result = num.add(2.5)
        assert result._value == 8.0

    def test_add_with_int(self):
        """Тест сложения Number с int"""
        num = Number(5.5)
        result = num.add(3)
        assert result._value == 8.5

    def test_divide_with_number(self):
        """Тест деления двух Number объектов"""
        num1 = Number(10.0)
        num2 = Number(2.0)
        result = num1.divide(num2)
        assert result._value == 5.0

    def test_divide_with_float(self):
        """Тест деления Number на float"""
        num = Number(10.0)
        result = num.divide(2.5)
        assert result._value == 4.0

    def test_divide_by_zero_number(self):
        """Тест деления на ноль (Number)"""
        num1 = Number(10.0)
        num2 = Number(0.0)
        with pytest.raises(ValueError, match="Деление на ноль невозможно"):
            num1.divide(num2)

    def test_divide_by_zero_float(self):
        """Тест деления на ноль (float)"""
        num = Number(10.0)
        with pytest.raises(ValueError, match="Деление на ноль невозможно"):
            num.divide(0.0)

    def test_str_representation(self):
        """Тест строкового представления"""
        num = Number(3.14)
        assert str(num) == "3.14"

    def test_repr_representation(self):
        """Тест repr представления"""
        num = Number(3.14)
        assert repr(num) == "Number(3.14)"


class TestReal:
    """Тесты для производного класса Real"""

    def test_inheritance(self):
        """Тест наследования от Number"""
        real = Real(5.0)
        assert isinstance(real, Number)

    def test_power_with_real(self):
        """Тест возведения в степень (Real объект)"""
        real1 = Real(8.0)
        real2 = Real(2.0)
        result = real1.power(real2)
        assert result._value == 64.0

    def test_power_with_float(self):
        """Тест возведения в степень (float)"""
        real = Real(4.0)
        result = real.power(0.5)
        assert result._value == 2.0

    def test_power_with_int(self):
        """Тест возведения в степень (int)"""
        real = Real(2.0)
        result = real.power(3)
        assert result._value == 8.0

    def test_logarithm_natural(self):
        """Тест натурального логарифма"""
        real = Real(math.e)
        result = real.logarithm()
        assert abs(result._value - 1.0) < 1e-10

    def test_logarithm_with_base_real(self):
        """Тест логарифма с основанием (Real объект)"""
        real_num = Real(8.0)
        real_base = Real(2.0)
        result = real_num.logarithm(real_base)
        assert result._value == 3.0

    def test_logarithm_with_base_float(self):
        """Тест логарифма с основанием (float)"""
        real = Real(100.0)
        result = real.logarithm(10.0)
        assert result._value == 2.0

    def test_logarithm_with_base_int(self):
        """Тест логарифма с основанием (int)"""
        real = Real(8.0)
        result = real.logarithm(2)
        assert result._value == 3.0

    def test_logarithm_negative_number(self):
        """Тест логарифма отрицательного числа"""
        real = Real(-5.0)
        with pytest.raises(
            ValueError, match="Логарифм определен только для положительных чисел"
        ):
            real.logarithm()

    def test_logarithm_zero_number(self):
        """Тест логарифма нуля"""
        real = Real(0.0)
        with pytest.raises(
            ValueError, match="Логарифм определен только для положительных чисел"
        ):
            real.logarithm()

    def test_logarithm_invalid_base_zero(self):
        """Тест логарифма с нулевым основанием"""
        real = Real(10.0)
        with pytest.raises(ValueError, match="Некорректные значения для логарифма"):
            real.logarithm(0.0)

    def test_logarithm_invalid_base_negative(self):
        """Тест логарифма с отрицательным основанием"""
        real = Real(10.0)
        with pytest.raises(ValueError, match="Некорректные значения для логарифма"):
            real.logarithm(-2.0)

    def test_logarithm_invalid_base_one(self):
        """Тест логарифма с основанием 1"""
        real = Real(10.0)
        with pytest.raises(ValueError, match="Некорректные значения для логарифма"):
            real.logarithm(1.0)

    def test_inherited_methods(self):
        """Тест унаследованных методов от Number"""
        real1 = Real(6.0)
        real2 = Real(2.0)

        result_add = real1.add(real2)
        assert result_add._value == 8.0

        result_div = real1.divide(real2)
        assert result_div._value == 3.0

    def test_repr_representation(self):
        """Тест repr представления"""
        real = Real(3.14)
        assert repr(real) == "Real(3.14)"


class TestIntegration:
    """Интеграционные тесты для взаимодействия классов"""

    def test_number_real_interaction(self):
        """Тест взаимодействия между Number и Real"""
        num = Number(5.0)
        real = Real(3.0)

        result1 = num.add(real)
        assert result1._value == 8.0

        result2 = real.add(num)
        assert result2._value == 8.0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
