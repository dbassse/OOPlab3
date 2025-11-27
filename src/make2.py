from .task_package.zad2 import Binary, Decimal, Reader, demonstrate_output


def main() -> None:
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


if __name__ == "__main__":
    main()
