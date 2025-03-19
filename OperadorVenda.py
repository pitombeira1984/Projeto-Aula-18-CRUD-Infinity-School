import sqlite3

class OperadorVenda:
    def __init__(self, id_produto, qt_vendida, data_venda):
        self.id_produto = id_produto
        self.qt_vendida = qt_vendida
        self.data_venda = data_venda
        
    def salvarVenda(self):
        try:
            conn = sqlite3.connect("loja.db")
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO vendas (id_produto, qt_vendida, data_venda)
                VALUES (?, ?, ?);
            """, (self.id_produto, self.qt_vendida, self.data_venda))
            conn.commit()
            cur.close()
            conn.close()
            print("Venda cadastrada com sucesso!")
        except Exception as e:
            print(f"Erro ao cadastrar venda: {e}")
    
    @staticmethod
    def listarVendas():
        try:
            conn = sqlite3.connect("loja.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM vendas;")
            vendas = cur.fetchall()
            cur.close()
            conn.close()
            for venda in vendas:
                print(venda)
        except Exception as e:
            print(f"Erro ao listar vendas: {e}")
    
    @staticmethod
    def deletarVenda(id):
        try:
            conn = sqlite3.connect("loja.db")
            cur = conn.cursor()
            cur.execute("DELETE FROM vendas WHERE id = ?;", (id,))
            conn.commit()
            cur.close()
            conn.close()
            print("Venda deletada com sucesso!")
        except Exception as e:
            print(f"Erro ao deletar venda: {e}")
    
    @staticmethod
    def atualizarVenda(id, id_produto, qt_vendida, data_venda):
        try:
            conn = sqlite3.connect("loja.db")
            cur = conn.cursor()
            cur.execute("""
                UPDATE vendas SET id_produto = ?, qt_vendida = ?, data_venda = ? WHERE id = ?;
            """, (id_produto, qt_vendida, data_venda, id))
            conn.commit()
            cur.close()
            conn.close()
            print("Venda atualizada com sucesso!")
        except Exception as e:
            print(f"Erro ao atualizar venda: {e}")
            
            

