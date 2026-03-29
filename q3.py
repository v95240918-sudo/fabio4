def main():
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))

    print("MDC =", calcular_mdc(a, b))


def calcular_mdc(a, b):
    menor = a
    if b < menor:
        menor = b

    mdc = 1
    i = 1

    while i <= menor:
        if a % i == 0 and b % i == 0:
            mdc = i
        i += 1

    return mdc


if __name__ == "__main__":
    main()