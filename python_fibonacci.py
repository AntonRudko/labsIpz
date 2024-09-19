def fibonacci(n):
    if n <= 0:
        return "Число повинно бути більше нуля"
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b


def main():
    print("Консольний застосунок для обчислення чисел Фібоначчі")

    try:
        n = int(input("Введіть порядковий номер числа Фібоначчі: "))
        result = fibonacci(n)
        print(f"{n}-е число Фібоначчі: {result}")
    except ValueError:
        print("Будь ласка, введіть коректне число.")


if __name__ == "__main__":
    main()
