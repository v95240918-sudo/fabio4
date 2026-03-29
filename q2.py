def main():
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))

    print("MMC =", calcular_mmc(a, b))


def calcular_mmc(a, b):
    maior = a
    if b > maior:
        maior = b

    mmc = maior

    while True:
        if mmc % a == 0 and mmc % b == 0:
            return mmc
        mmc += 1


if __name__ == "__main__":
    main()