def main():
    processar_produtos()


def processar_produtos():
    nome = input("Nome do produto (FIM para sair): ")

    while nome != "FIM":
        preco = float(input("Preço: "))
        qtd = int(input("Quantidade: "))

        total = preco * qtd

        if qtd <= 10:
            pass
        elif qtd <= 20:
            total *= 0.9
        elif qtd <= 50:
            total *= 0.8
        else:
            total *= 0.75

        print("Produto:", nome)
        print("Total:", total)

        nome = input("Nome do produto (FIM para sair): ")


if __name__ == "__main__":
    main()