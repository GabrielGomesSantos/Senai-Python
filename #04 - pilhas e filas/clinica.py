import random as r
import tkinter as tk

fila = []
lista = [1, 2, 3, 4, 5]
sala = r.choice(lista)

def registro(dados):
    paciente = dados
    fila.append(paciente)

def chamar():
    if fila:
        paciente_chamado = fila.pop(0)
        resultado.set(f"{paciente_chamado[0]}, o doutor está chamando na sala {sala}")
        atualizar_lista()
    else:
        resultado.set("A fila está vazia. Não há pacientes para chamar.")

def tamanho():
    resultado.set(f"A fila conta atualmente com {len(fila)} pacientes")

def adicionar_paciente():
    nome = entry_nome.get()
    numero = len(fila) + 1
    dados = [nome, numero]
    registro(dados)
    entry_nome.delete(0, tk.END)
    atualizar_lista()

def atualizar_lista():
    lista_pacientes.delete(0, tk.END)
    for paciente in fila:
        lista_pacientes.insert(tk.END, paciente[0])

# Cria a interface gráfica principal
janela_principal = tk.Tk()
janela_principal.title("Sistema de Fila")
janela_principal.geometry("400x400")

# Define o fundo azul claro
fundo_azul = tk.Frame(janela_principal,)
fundo_azul.place(relwidth=1, relheight=1)

# Lista de pacientes
lista_pacientes = tk.Listbox(fundo_azul)
lista_pacientes.pack(pady=10)

# Entrada de nome
label_nome = tk.Label(fundo_azul, text="Nome do paciente:")
label_nome.pack()
entry_nome = tk.Entry(fundo_azul)
entry_nome.pack()

# Botão para adicionar paciente
botao_adicionar = tk.Button(fundo_azul, text="Adicionar paciente à fila", command=adicionar_paciente)
botao_adicionar.pack()

# Botão para chamar paciente
botao_chamar = tk.Button(fundo_azul, text="Chamar próximo paciente", command=chamar)
botao_chamar.pack()

# Botão para mostrar tamanho da fila
botao_tamanho = tk.Button(fundo_azul, text="Mostrar total de pacientes na fila", command=tamanho)
botao_tamanho.pack()

# Variável para mostrar resultado
resultado = tk.StringVar()
resultado.set("")
label_resultado = tk.Label(fundo_azul, textvariable=resultado)
label_resultado.pack()

janela_principal.mainloop()
