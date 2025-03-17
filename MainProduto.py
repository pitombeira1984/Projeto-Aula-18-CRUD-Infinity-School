import sqlite3
from OperadorProduto import Produto


def main():
    while True:
        print("1. Cadastrar produto")
        print("2. Listar produtos")
        print("3. Deletar produto")
        print("4. Atualizar produto")
        print("5. Sair")

        opcao = int(input("Opção: "))
        if opcao == 1:
            nome = input("Nome: ")
            descricao = input("Descrição: ")
            qt_disponivel = int(input("Quantidade disponível: "))
            preco = float(input("Preço: "))
            produto = Produto(nome, descricao, qt_disponivel, preco)
            produto.salvar()
        elif opcao == 2:
            Produto.listar()
        elif opcao == 3:
            Produto.deletar(input("ID do produto: "))
        elif opcao == 4:
            Produto.atualizar(
                input("ID do produto: "),
                input("Nome: "),
                input("Descrição: "),
                int(input("Quantidade disponível: ")),
                float(input("Preço: ")),
            )
        elif opcao == 5:
            break
        else:
            print("Opção inválida")
main()



