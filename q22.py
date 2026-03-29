def main():
    a = int(input("Digite o dividendo: "))
    b = int(input("Digite o divisor: "))

    quociente, resto = dividir(a, b)

    print("Quociente:", quociente)
    print("Resto:", resto)


def dividir(a, b):
    quociente = 0

    while a >= b:
        a -= b
        quociente += 1

    return quociente, a


if __name__ == "__main__":
    main()