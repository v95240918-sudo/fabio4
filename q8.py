def main():
    x = int(input("Digite o valor de X: "))

    anterior = int(input("Digite um número: "))
    atual = int(input("Digite outro número: "))

    while anterior + atual != x:
        anterior = atual
        atual = int(input("Digite outro número: "))


if __name__ == "__main__":
    main()