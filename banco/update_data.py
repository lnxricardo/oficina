import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

id_cliente = 1
novo_fone = '32-99142-9107'
novo_criado_em = '2019-01-09'


# alterando a tabela

cursor.execute("""
        UPDATE clientes
        SET fone = ?, criado_em = ?
        WHERE id = ?
        """, (novo_fone, novo_criado_em, id_cliente))

conn.commit()

print('Dados atualizados com sucesso!!')


conn.close()
