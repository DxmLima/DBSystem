import tkinter as tk
import sqlite3
import pandas as pd



def cadastrar_cliente():

    cx = sqlite3.connect('Clientes.db')

    c = cx.cursor()

    c.execute(" INSERT INTO clientesmk2 VALUES(:nome, :dn, :adress, :rg, :cpf)",
              {
                  'nome': entry_nome.get(),
                  'dn': entry_dn.get(),
                  'adress': entry_adress.get(),
                  'rg': entry_rg.get(),
                  'cpf': entry_cpf.get()
              }
              )

    cx.commit()

    cx.close()

    entry_nome.delete(0, "end")
    entry_dn.delete(0, "end")
    entry_adress.delete(0, "end")
    entry_rg.delete(0, "end")
    entry_cpf.delete(0, "end")


def exporta_clientes():
    conexao = sqlite3.connect('clientes.db')

    c = conexao.cursor()

    c.execute("SELECT *, oid FROM clientesmk2")
    clientes_cadastrados = c.fetchall()
    clientes_cadastrados = pd.DataFrame(clientes_cadastrados, columns=[
                                        'Nome', 'Data de Nascimento', 'Endereço', 'RG', 'CPF', 'DBS'])
    clientes_cadastrados.to_html("clientesinfo.html")

    conexao.close()


window = tk.Tk()
window.title("Ferramenta de Cadastro")

label_nome = tk.Label(window, text='Nome Completo')
label_nome.grid(row=0, column=0, padx=10, pady=10)

label_dn = tk.Label(window, text='Data de Nascimento')
label_dn.grid(row=1, column=0, padx=10, pady=10)

label_adress = tk.Label(window, text='Endereço')
label_adress.grid(row=2, column=0, padx=10, pady=10)

label_rg = tk.Label(window, text='RG')
label_rg.grid(row=3, column=0, padx=10, pady=10)

label_cpf = tk.Label(window, text='CPF')
label_cpf.grid(row=4, column=0, padx=10, pady=10)

# Entradas

entry_nome = tk.Entry(window, text='Nome Completo', width=30)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

entry_dn = tk.Entry(window, text='Data de Nascimento', width=30)
entry_dn.grid(row=1, column=1, padx=10, pady=10)

entry_adress = tk.Entry(window, text='Endereço', width=30)
entry_adress.grid(row=2, column=1, padx=10, pady=10)

entry_rg = tk.Entry(window, text='RG', width=30)
entry_rg.grid(row=3, column=1, padx=10, pady=10)

entry_cpf = tk.Entry(window, text='CPF', width=30)
entry_cpf.grid(row=4, column=1, padx=10, pady=10)

# Botões

botao_cadastro = tk.Button(
    window, text='Cadastrar Cliente', command=cadastrar_cliente)
botao_cadastro.grid(row=5, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

botao_exportar = tk.Button(
    window, text='Exportar Base', command=exporta_clientes)
botao_exportar.grid(row=6, column=0, padx=10, pady=10, columnspan=2, ipadx=80)


window.mainloop()
