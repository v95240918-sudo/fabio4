def main():
    dias = calcular_dias_pagamento()
    print("Dias úteis necessários:", dias)


def calcular_dias_pagamento():
    saldo = 3000
    dias = 0

    while saldo > 0:
        saldo += saldo * 0.0085  # juros diário
        saldo -= 200             # pagamento
        dias += 1

    return dias


if __name__ == "__main__":
    main()