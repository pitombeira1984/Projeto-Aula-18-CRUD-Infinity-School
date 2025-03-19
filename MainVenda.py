import sqlite3
from OperadorVenda import OperadorVenda

def main():
    while True:
        print("1 - Cadastrar venda")
        print("2 - Listar vendas")
        print("3 - Deletar venda")
        print("4 - Atualizar venda")
        print("5 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        now = sqlite3.connect("loja.db").cursor().execute("SELECT CURRENT_TIMESTAMP;").fetchone()[0]
        
        if opcao == "1":
            id_produto = int(input("ID do produto: "))
            qt_vendida = int(input("Quantidade vendida: "))
            data_venda = now
            venda = OperadorVenda(id_produto, qt_vendida, data_venda)
            venda.salvarVenda()
        elif opcao == "2":
            OperadorVenda.listarVendas()
        elif opcao == "3":
            OperadorVenda.deletarVenda(input("ID da venda: "))
        elif opcao == "4":
            OperadorVenda.atualizarVenda(
                input("ID da venda: "),
                input("ID do produto atualizado: "),
                input("Quantidade vendida atualizado: "),
                input("Data da venda atuali: ")
            )
        elif opcao == "5":
            break
        else:
            print("Opção inválida")
main()
        

