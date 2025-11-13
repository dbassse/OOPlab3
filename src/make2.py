from src.task_package.zad2 import Binary, Decimal, demonstrate_output


def main() -> None:
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


if __name__ == "__main__":
    main()
