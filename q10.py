def main():
    peso_carga = calcular_carga()
    passageiros, bagagens, peso_passageiros = calcular_passageiros()

    combustivel_max = calcular_combustivel(peso_carga, peso_passageiros)

    print("Passageiros:", passageiros)
    print("Bagagens:", bagagens)
    print("Peso passageiros:", peso_passageiros)
    print("Peso carga:", peso_carga)
    print("Combustível máximo (L):", combustivel_max)

    if combustivel_max >= 10000:
        print("Decolagem autorizada")
    else:
        print("Decolagem NÃO autorizada")


def calcular_carga():
    total = 0
    n = int(input("Quantidade de containers: "))

    i = 1
    while i <= n:
        peso = float(input("Peso do container: "))
        total += peso
        i += 1

    return total


def calcular_passageiros():
    total_passageiros = 0
    total_bagagens = 0

    bilhete = int(input("Número do bilhete (0 para sair): "))

    while bilhete != 0:
        bagagens = int(input("Quantidade de bagagens: "))

        total_passageiros += 1
        total_bagagens += bagagens

        bilhete = int(input("Número do bilhete (0 para sair): "))

    peso_passageiros = (total_passageiros * 70) + (total_bagagens * 10)

    return total_passageiros, total_bagagens, peso_passageiros


def calcular_combustivel(peso_carga, peso_passageiros):
    peso_total_max = 500000

    peso_restante = peso_total_max - (peso_carga + peso_passageiros)

    combustivel_litros = peso_restante / 1.5

    return combustivel_litros


if __name__ == "__main__":
    main()