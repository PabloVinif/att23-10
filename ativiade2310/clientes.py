import sqlite3
from pyDatalog import pyDatalog


pyDatalog.create_terms('cliente_pedido, Cliente, Pedido, fez_pedido')

def carregar_dados_do_banco(nome_banco):
   
    conexao = sqlite3.connect(nome_banco)
    cursor = conexao.cursor()

   
    cursor.execute("SELECT cliente, pedido FROM clientes")
    registros = cursor.fetchall()

   
    conexao.close()

   
    for cliente, pedido in registros:
        +cliente_pedido(cliente, pedido)  
        print(f"Fato adicionado: cliente_pedido({cliente}, {pedido})") 


fez_pedido(Cliente, Pedido) <= cliente_pedido(Cliente, Pedido)


carregar_dados_do_banco('clientes.db')


clientes_notebook = fez_pedido(Cliente, 'Notebook')


print("\nClientes que pediram um Notebook:")
for resultado in clientes_notebook:
    print(f"{resultado[0]} pediu Notebook")


clientes_livro = fez_pedido(Cliente, 'Livro')


print("\nClientes que pediram um Livro:")
for resultado in clientes_livro:
    print(f"{resultado[0]} pediu Livro")
