def main():
    analisar_bois()


def analisar_bois():
    codigo = int(input("Código do boi (0 para sair): "))

    mais_gordo = 0
    mais_magro = 0
    maior_peso = -1
    menor_peso = 9999

    while codigo != 0:
        peso = float(input("Peso do boi: "))

        if peso > maior_peso:
            maior_peso = peso
            mais_gordo = codigo

        if peso < menor_peso:
            menor_peso = peso
            mais_magro = codigo

        codigo = int(input("Código do boi (0 para sair): "))

    print("Boi mais gordo:", mais_gordo, maior_peso)
    print("Boi mais magro:", mais_magro, menor_peso)


if __name__ == "__main__":
    main()