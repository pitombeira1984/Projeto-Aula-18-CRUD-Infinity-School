import sqlite3

def venda():
    try:
        banco = sqlite3.connect('banco.db')
        cursor = banco.cursor()
        cursor.execute("SELECT * FROM vendas")
        print(cursor.fetchall())
        banco.commit()
        banco.close()
        print("Venda realizada com sucesso!")
    except Exception as e:
        print(f"Erro ao realizar venda: {e}")


