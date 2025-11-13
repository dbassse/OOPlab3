import os
import sys
from io import StringIO
from unittest.mock import patch

import pytest

from task_package.zad2 import Binary, Decimal, Integer, demonstrate_output

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))  # noqa: E402


class TestDecimal:
    def test_initialization_default(self):
        dec = Decimal()
        assert dec.digits == [0]

    def test_initialization_with_digits(self):
        dec = Decimal([1, 2, 3])
        assert dec.digits == [1, 2, 3]

    def test_initialization_validation_valid(self):
        dec = Decimal([1, 2, 3, 4, 5])
        assert dec.digits == [1, 2, 3, 4, 5]

    def test_initialization_validation_invalid(self):
        with pytest.raises(ValueError, match="Цифры должны быть в диапазоне 0-9"):
            Decimal([10, 11])

    def test_to_int(self):
        dec = Decimal([1, 2, 3])
        assert dec._to_int() == 123

    def test_from_int_positive(self):
        dec = Decimal._from_int(456)
        assert dec.digits == [4, 5, 6]

    def test_from_int_zero(self):
        dec = Decimal._from_int(0)
        assert dec.digits == [0]

    def test_from_int_negative(self):
        dec = Decimal._from_int(-789)
        assert dec.digits == [7, 8, 9]

    @patch("builtins.input", return_value="123")
    def test_input_valid(self, mock_input):
        dec = Decimal()
        dec.input()
        assert dec.digits == [1, 2, 3]

    @patch("builtins.input", return_value="abc")
    def test_input_invalid(self, mock_input):
        dec = Decimal()
        with pytest.raises(ValueError, match="Некорректный ввод десятичного числа"):
            dec.input()

    @patch("sys.stdout", new_callable=StringIO)
    def test_output(self, mock_stdout):
        dec = Decimal([1, 2, 3])
        dec.output()
        output = mock_stdout.getvalue()
        assert "Десятичное число: 123" in output
        assert "Представление в виде массива цифр: [1, 2, 3]" in output

    def test_add(self):
        """Тест сложения"""
        dec1 = Decimal([1, 2])
        dec2 = Decimal([3, 4])
        result = dec1.add(dec2)
        assert result._to_int() == 46

    def test_add_type_error(self):
        dec = Decimal([1, 2])
        bin_obj = Binary([1, 0])
        with pytest.raises(TypeError, match="Можно складывать только десятичные числа"):
            dec.add(bin_obj)

    def test_subtract(self):
        dec1 = Decimal([5, 0])
        dec2 = Decimal([2, 5])
        result = dec1.subtract(dec2)
        assert result._to_int() == 25

    def test_multiply(self):
        dec1 = Decimal([1, 2])
        dec2 = Decimal([3])
        result = dec1.multiply(dec2)
        assert result._to_int() == 36

    def test_divide(self):
        dec1 = Decimal([1, 0])
        dec2 = Decimal([2])
        result = dec1.divide(dec2)
        assert result._to_int() == 5

    def test_divide_by_zero(self):
        dec1 = Decimal([1, 0])
        dec2 = Decimal([0])
        with pytest.raises(ValueError, match="Деление на ноль"):
            dec1.divide(dec2)


class TestBinary:
    def test_initialization_default(self):
        bin_obj = Binary()
        assert bin_obj.digits == [0]

    def test_initialization_with_bits(self):
        bin_obj = Binary([1, 0, 1])
        assert bin_obj.digits == [1, 0, 1]

    def test_initialization_validation_valid(self):
        bin_obj = Binary([1, 0, 1, 0, 1])
        assert bin_obj.digits == [1, 0, 1, 0, 1]

    def test_initialization_validation_invalid(self):
        with pytest.raises(ValueError, match="Биты должны быть 0 или 1"):
            Binary([1, 2, 3])

    def test_to_int(self):
        bin_obj = Binary([1, 0, 1, 0])
        assert bin_obj._to_int() == 10

    def test_from_int_positive(self):
        bin_obj = Binary._from_int(5)
        assert bin_obj.digits == [1, 0, 1]

    def test_from_int_zero(self):
        bin_obj = Binary._from_int(0)
        assert bin_obj.digits == [0]

    def test_from_int_negative(self):
        bin_obj = Binary._from_int(-3)
        assert bin_obj.digits == [1, 1]

    @patch("builtins.input", return_value="1010")
    def test_input_valid(self, mock_input):
        bin_obj = Binary()
        bin_obj.input()
        assert bin_obj.digits == [1, 0, 1, 0]

    @patch("builtins.input", return_value="1021")
    def test_input_invalid(self, mock_input):
        bin_obj = Binary()
        with pytest.raises(ValueError, match="Некорректный ввод двоичного числа"):
            bin_obj.input()

    @patch("sys.stdout", new_callable=StringIO)
    def test_output(self, mock_stdout):
        bin_obj = Binary([1, 0, 1, 0])
        bin_obj.output()
        output = mock_stdout.getvalue()
        assert "Двоичное число: 1010" in output
        assert "Десятичное значение: 10" in output
        assert "Представление в виде массива битов: [1, 0, 1, 0]" in output

    def test_add(self):
        bin1 = Binary([1, 0, 1])  # 5
        bin2 = Binary([1, 1])  # 3
        result = bin1.add(bin2)  # 8
        assert result._to_int() == 8
        assert result.digits == [1, 0, 0, 0]

    def test_add_type_error(self):
        bin_obj = Binary([1, 0])
        dec = Decimal([1, 2])
        with pytest.raises(TypeError, match="Можно складывать только двоичные числа"):
            bin_obj.add(dec)

    def test_subtract(self):
        bin1 = Binary([1, 0, 1, 0])  # 10
        bin2 = Binary([1, 1, 0])  # 6
        result = bin1.subtract(bin2)  # 4
        assert result._to_int() == 4
        assert result.digits == [1, 0, 0]

    def test_multiply(self):
        bin1 = Binary([1, 0, 1])  # 5
        bin2 = Binary([1, 0])  # 2
        result = bin1.multiply(bin2)  # 10
        assert result._to_int() == 10
        assert result.digits == [1, 0, 1, 0]

    def test_divide(self):
        bin1 = Binary([1, 0, 1, 0])  # 10
        bin2 = Binary([1, 0])  # 2
        result = bin1.divide(bin2)  # 5
        assert result._to_int() == 5
        assert result.digits == [1, 0, 1]

    def test_divide_by_zero(self):
        bin1 = Binary([1, 0, 1])
        bin2 = Binary([0])
        with pytest.raises(ValueError, match="Деление на ноль"):
            bin1.divide(bin2)


class TestIntegerABC:
    def test_abstract_methods(self):
        """Тест, что абстрактные методы действительно абстрактные"""
        with pytest.raises(TypeError):
            Integer()


class TestDemonstrateOutput:
    @patch("sys.stdout", new_callable=StringIO)
    def test_demonstrate_output_decimal(self, mock_stdout):
        """Тест виртуального вызова для Decimal"""
        dec = Decimal([1, 2, 3])
        demonstrate_output(dec)
        output = mock_stdout.getvalue()
        assert "Виртуальный вызов:" in output
        assert "Десятичное число: 123" in output

    @patch("sys.stdout", new_callable=StringIO)
    def test_demonstrate_output_binary(self, mock_stdout):
        """Тест виртуального вызова для Binary"""
        bin_obj = Binary([1, 0, 1, 0])
        demonstrate_output(bin_obj)
        output = mock_stdout.getvalue()
        assert "Виртуальный вызов:" in output
        assert "Двоичное число: 1010" in output


class TestIntegration:
    def test_decimal_operations_chain(self):
        """Тест цепочки операций для Decimal"""

        a = Decimal([1, 0])
        b = Decimal([5])
        c = Decimal([2])
        d = Decimal([8])
        e = Decimal([4])

        result1 = a.add(b)
        result2 = result1.multiply(c)
        result3 = d.divide(e)
        result4 = result2.subtract(result3)

        assert result4._to_int() == 28

    def test_binary_operations_chain(self):
        """Тест цепочки операций для Binary"""

        a = Binary([1, 0, 1])
        b = Binary([1, 1])
        c = Binary([1, 0])
        d = Binary([1, 0, 0])

        result1 = a.add(b)
        result2 = result1.multiply(c)
        result3 = d.divide(c)
        result4 = result2.subtract(result3)

        assert result4._to_int() == 14
        assert result4.digits == [1, 1, 1, 0]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
