def main():
    numero = int(input("Digite um número: "))
    print("Quantidade de dígitos:", contar_digitos(numero))


def contar_digitos(numero):
    if numero == 0:
        return 1

    contador = 0
    while numero != 0:
        numero = numero // 10
        contador += 1

    return contador


if __name__ == "__main__":
    main()