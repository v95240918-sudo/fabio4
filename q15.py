def main():
    numero = int(input("Digite um número (0 a 255): "))

    print("Binário:", decimal_para_binario(numero))
    print("Hexadecimal:", decimal_para_hex(numero))


def decimal_para_binario(n):
    if n == 0:
        return "0"

    resultado = ""
    while n > 0:
        resultado = str(n % 2) + resultado
        n = n // 2

    return resultado


def decimal_para_hex(n):
    if n == 0:
        return "0"

    hexa = "0123456789ABCDEF"
    resultado = ""

    while n > 0:
        resultado = hexa[n % 16] + resultado
        n = n // 16

    return resultado


if __name__ == "__main__":
    main()