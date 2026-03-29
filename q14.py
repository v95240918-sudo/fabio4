def main():
    resultados = pesquisa()

    total = resultados["total"]

    if total > 0:
        print("Serra:", resultados["45"] * 100 / total, "%")
        print("Dilma:", resultados["13"] * 100 / total, "%")
        print("Ciro:", resultados["23"] * 100 / total, "%")
        print("Outros:", resultados["98"] * 100 / total, "%")
        print("Indecisos:", resultados["99"] * 100 / total, "%")
        print("Nulos:", resultados["0"] * 100 / total, "%")

        if (resultados["45"] > total/2 or 
            resultados["13"] > total/2 or 
            resultados["23"] > total/2):
            print("Não haverá 2º turno")
        else:
            print("Haverá 2º turno")


def pesquisa():
    votos = {"45":0, "13":0, "23":0, "98":0, "99":0, "0":0}
    total = 0

    voto = int(input("Voto (-1 para sair): "))

    while voto != -1:
        if str(voto) in votos:
            votos[str(voto)] += 1
            total += 1

        voto = int(input("Voto (-1 para sair): "))

    votos["total"] = total
    return votos


if __name__ == "__main__":
    main()