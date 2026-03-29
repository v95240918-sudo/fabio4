def main():
    numero = int(input("Digite um número (0 a 999): "))
    print("Romano:", decimal_para_romano(numero))


def decimal_para_romano(n):
    valores = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]

    resultado = ""

    i = 0
    while i < len(valores):
        valor, simbolo = valores[i]

        while n >= valor:
            resultado += simbolo
            n -= valor

        i += 1

    return resultado


if __name__ == "__main__":
    main()