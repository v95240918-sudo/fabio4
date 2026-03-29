def main():
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))

    print("Resultado:", multiplicar(a, b))


def multiplicar(a, b):
    resultado = 0
    i = 0

    negativo = False
    if b < 0:
        b = -b
        negativo = True

    while i < b:
        resultado += a
        i += 1

    if negativo:
        resultado = -resultado

    return resultado


if __name__ == "__main__":
    main()