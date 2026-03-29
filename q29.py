def main():
    calcular_investimento()


def calcular_investimento():
    deposito = float(input("Depósito mensal: "))
    taxa = float(input("Taxa (%): ")) / 100

    continuar = 'S'

    while continuar == 'S':
        saldo = 0
        mes = 1

        while mes <= 12:
            saldo += deposito
            saldo += saldo * taxa
            mes += 1

        print("Saldo após 1 ano:", saldo)

        continuar = input("Deseja continuar (S/N)? ").upper()


if __name__ == "__main__":
    main()