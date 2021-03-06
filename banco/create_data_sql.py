import sqlite3

conn = sqlite3.connect('clientes.db')

cursor = conn.cursor()

# inserindo dados na tablea

cursor.execute("""
        INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
        VALUES ('Ricardo Assis', 35, '00000000000', 'ricardoti@outlook.com', '11-5816-6854', 'São Paulo', 'SP', '2018-06-08')
        """)
cursor.execute("""
        INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
        VALUES ('Luana Melo', 29, '11111111111', 'luanakta@gmail.com', '32-3232-5874', 'Juiz de Fora', 'MG', '2016-07-09')
        """)
cursor.execute("""
        INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
        VALUES ('Laura Melo', 15, '22222222222', 'laurinha@gmail.com', '32-98989-5544', 'Juiz de Fora', 'MG', '2023-05-09')
        """)
cursor.execute("""
        INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
        VALUES ('Arthur Melo', 11, '33333333333', 'tuca@outlook.com', '98547-9856', 'Juiz de Fora', 'MG', '2025-07-07')
        """)

# gravando no bd

conn.commit()

print('Dados inseridos com sucesso!')

# fechando a conexão
conn.close()
