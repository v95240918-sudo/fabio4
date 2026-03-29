def main():
    calcular_audiencia()


def calcular_audiencia():
    canais = {2:0, 4:0, 5:0, 7:0, 10:0}
    total = 0

    canal = int(input("Canal (0 para sair): "))

    while canal != 0:
        pessoas = int(input("Número de pessoas: "))

        if canal in canais:
            canais[canal] += pessoas
            total += pessoas

        canal = int(input("Canal (0 para sair): "))

    for c in canais:
        if total > 0:
            print("Canal", c, ":", canais[c]*100/total, "%")


if __name__ == "__main__":
    main()