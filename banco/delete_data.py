import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

cursor.execute("""
        SELECT * FROM clientes;
        """)




id_cliente = input('Digite o ID do cliente que dejesa deletar: ')

while id_cliente not in cursor.fetchall:
    id_cliente = input('Favor digitar uma ID válida: ')

cursor.execute("""
        DELETE FROM clientes
        WHERE id = ?
        """, (id_cliente,))

conn.commit()

print('Registro excluido com sucesso: ')

conn.close()


