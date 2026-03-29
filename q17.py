def main():
    analisar_candidatas()


def analisar_candidatas():
    nome = input("Nome (FIM para sair): ")

    mais_alta = ""
    mais_baixa = ""
    mais_gorda = ""
    mais_magra = ""

    maior_altura = -1
    menor_altura = 9999
    maior_peso = -1
    menor_peso = 9999

    while nome != "FIM":
        altura = float(input("Altura: "))
        peso = float(input("Peso: "))

        if altura > maior_altura:
            maior_altura = altura
            mais_alta = nome

        if altura < menor_altura:
            menor_altura = altura
            mais_baixa = nome

        if peso > maior_peso:
            maior_peso = peso
            mais_gorda = nome

        if peso < menor_peso:
            menor_peso = peso
            mais_magra = nome

        nome = input("Nome (FIM para sair): ")

    print("Mais alta:", mais_alta, maior_altura)
    print("Mais baixa:", mais_baixa, menor_altura)
    print("Mais gorda:", mais_gorda, maior_peso)
    print("Mais magra:", mais_magra, menor_peso)


if __name__ == "__main__":
    main()