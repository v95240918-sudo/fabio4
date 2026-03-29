def main():
    analisar_viagem()


def analisar_viagem():
    distancia_total = 0
    combustivel_total = 0

    distancia = float(input("Distância percorrida: "))
    combustivel = float(input("Combustível gasto: "))

    while distancia_total < 600 and combustivel_total < 50:
        distancia_total += distancia
        combustivel_total += combustivel

        if distancia_total >= 600 or combustivel_total >= 50:
            break

        distancia = float(input("Distância percorrida: "))
        combustivel = float(input("Combustível gasto: "))

    print("Distância total:", distancia_total)
    print("Combustível total:", combustivel_total)

    if distancia_total >= 600:
        print("Chegou ao destino")
    elif combustivel_total >= 50:
        print("Parou por falta de combustível")

    if combustivel_total > 0:
        print("Consumo (km/l):", distancia_total / combustivel_total)


if __name__ == "__main__":
    main()