def main():
    vencedor = partida_pingpong()
    print("Vencedor:", vencedor)


def partida_pingpong():
    p1 = 0
    p2 = 0

    jogador = int(input("Quem marcou (1 ou 2): "))

    while True:
        if jogador == 1:
            p1 += 1
        elif jogador == 2:
            p2 += 1

        if (p1 >= 21 or p2 >= 21) and abs(p1 - p2) >= 2:
            break

        jogador = int(input("Quem marcou (1 ou 2): "))

    if p1 > p2:
        return "Jogador 1"
    else:
        return "Jogador 2"


if __name__ == "__main__":
    main()