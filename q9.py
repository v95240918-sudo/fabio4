def main():
    pontos_a, pontos_b = calcular_pontos()

    print("Clube A:", pontos_a, "pontos")
    print("Clube B:", pontos_b, "pontos")

    if pontos_a > pontos_b:
        print("Clube A venceu")
    elif pontos_b > pontos_a:
        print("Clube B venceu")
    else:
        print("Empate")


def calcular_pontos():
    pontos_a = 0
    pontos_b = 0

    prova = int(input("Número da prova (0 para sair): "))
    qtd = int(input("Quantidade de nadadores: "))

    while prova != 0 or qtd != 0:
        i = 1
        while i <= qtd:
            nome = input("Nome: ")
            posicao = int(input("Posição: "))
            tempo = float(input("Tempo: "))
            clube = input("Clube (a/b): ")

            pontos = 0
            if posicao == 1:
                pontos = 9
            elif posicao == 2:
                pontos = 6
            elif posicao == 3:
                pontos = 4
            elif posicao == 4:
                pontos = 3

            if clube == 'a':
                pontos_a += pontos
            else:
                pontos_b += pontos

            i += 1

        prova = int(input("Número da prova (0 para sair): "))
        qtd = int(input("Quantidade de nadadores: "))

    return pontos_a, pontos_b


if __name__ == "__main__":
    main()