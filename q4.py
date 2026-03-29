def main():
    numero = float(input("Digite um número: "))
    resultado = dividir_por_dois(numero)

    print("Último valor antes de ficar menor que 1:", resultado)


def dividir_por_dois(numero):
    while numero >= 1:
        ultimo = numero
        numero = numero / 2

    return ultimo


if __name__ == "__main__":
    main()