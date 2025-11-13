from src.task_package.zad1 import Number, Real


def main() -> None:
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


if __name__ == "__main__":
    main()
