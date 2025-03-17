import sqlite3

class Produto:
    def __init__(self, nome, descricao, qt_disponivel, preco):
        self.nome = nome
        self.descricao = descricao
        self.qt_disponivel = qt_disponivel
        self.preco = preco

    def salvar(self):
        try:
            conn = sqlite3.connect("loja.db")
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO produtos (nome, descricao, qt_disponivel, preco)
                VALUES (?, ?, ?, ?);
            """, (self.nome, self.descricao, self.qt_disponivel, self.preco))
            conn.commit()
            cur.close()
            conn.close()
            print("Produto cadastrado com sucesso!")
        except Exception as e:
            print(f"Erro ao cadastrar produto: {e}")

    @staticmethod
    def listar():
        try:
            conn = sqlite3.connect("loja.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM produtos;")
            produtos = cur.fetchall()
            cur.close()
            conn.close()
            for produto in produtos:
                print(produto)
        except Exception as e:
            print(f"Erro ao listar produtos: {e}")

    @staticmethod
    def deletar(id):
        try:
            conn = sqlite3.connect("loja.db")
            cur = conn.cursor()
            cur.execute("DELETE FROM produtos WHERE id = ?;", (id,))
            conn.commit()
            cur.close()
            conn.close()
            print("Produto deletado com sucesso!")
        except Exception as e:
            print(f"Erro ao deletar produto: {e}")

    @staticmethod
    def atualizar(id, nome, descricao, qt_disponivel, preco):
        try:
            conn = sqlite3.connect("loja.db")
            cur = conn.cursor()
            cur.execute("""
                UPDATE produtos SET nome = ?, descricao = ?, qt_disponivel = ?, preco = ? WHERE id = ?;
            """, (nome, descricao, qt_disponivel, preco, id))
            conn.commit()
            cur.close()
            conn.close()
            print("Produto atualizado com sucesso!")
        except Exception as e:
            print(f"Erro ao atualizar produto: {e}")


