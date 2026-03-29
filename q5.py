def main():
    x = float(input("Digite o valor de X: "))
    n = int(input("Digite o valor de N: "))

    divisoes_sucessivas(x, n)


def divisoes_sucessivas(x, n):
    while n >= 2:
        resultado = x / n
        print("X /", n, "=", resultado)

        x = resultado
        n -= 1


if __name__ == "__main__":
    main()