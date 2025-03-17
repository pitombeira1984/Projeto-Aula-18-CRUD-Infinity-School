import sqlite3

try:
    conn = sqlite3.connect("loja.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT NOT NULL,
            qt_disponivel INTEGER DEFAULT 0,        
            preco REAL NOT NULL
        );
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS vendas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_produto INTEGER NOT NULL,
            qt_vendida INTEGER NOT NULL,
            data_venda TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (id_produto) REFERENCES produtos(id)
        );
    """)
    cur.close()
    conn.close()
except:
    print("Erro ao criar tabela")

