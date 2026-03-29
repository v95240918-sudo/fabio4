def main():
    primeiro = int(input("Digite o primeiro número: "))
    numero = int(input("Digite outro número: "))

    while numero != primeiro:
        numero = int(input("Digite outro número: "))

    print("Número repetido encontrado!")


if __name__ == "__main__":
    main()