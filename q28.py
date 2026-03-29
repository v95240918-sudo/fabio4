def main():
    jogar()


def jogar():
    import random
    numero = random.randint(1, 100)

    tentativas = 0
    palpite = int(input("Digite um número: "))

    while palpite != numero:
        if palpite < numero:
            print("Maior")
        else:
            print("Menor")

        tentativas += 1
        palpite = int(input("Digite outro número: "))

    tentativas += 1
    print("Acertou em", tentativas, "tentativas")


if __name__ == "__main__":
    main()