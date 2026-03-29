def main():
    numero = int(input("Digite um número (0 para parar): "))

    while numero != 0:
        mostrar_divisores(numero)
        numero = int(input("Digite outro número (0 para parar): "))


def mostrar_divisores(numero):
    print("Número:", numero)
    print("Divisores:", end=" ")

    i = 1
    while i <= numero:
        if numero % i == 0:
            print(i, end=" ")
        i += 1

    print("\n")


if __name__ == "__main__":
    main()