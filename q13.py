def main():
    soma_antiga, soma_nova = calcular_salarios()

    print("Soma salários antigos:", soma_antiga)
    print("Soma salários novos:", soma_nova)
    print("Diferença:", soma_nova - soma_antiga)


def calcular_salarios():
    soma_antiga = 0
    soma_nova = 0

    salario = float(input("Salário (0 para sair): "))

    while salario != 0:
        soma_antiga += salario

        if salario <= 2999.99:
            novo = salario * 1.25
        elif salario <= 5999.99:
            novo = salario * 1.20
        elif salario <= 9999.99:
            novo = salario * 1.15
        else:
            novo = salario * 1.10

        soma_nova += novo

        print("Novo salário:", novo)

        salario = float(input("Salário (0 para sair): "))

    return soma_antiga, soma_nova


if __name__ == "__main__":
    main()