import sqlite3
from OperadorVenda import vender

def main():
   while True:
       print("1. Vender")
       print("2. Sair")

       opcao = int(input("Opção: "))
       if opcao == 1:
           vender()
       elif opcao == 2:
           break
       else:
           print("Opção inválida")
main()