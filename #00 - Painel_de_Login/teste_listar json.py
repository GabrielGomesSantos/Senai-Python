import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk

# Variável global para rastrear o modo
dark_mode = False

def toggle_dark_mode():
    global dark_mode
    dark_mode = not dark_mode
    if dark_mode:
        set_dark_mode(usuario_label, senha_label, login_button, resultado_label, dark_button)
    else:
        set_light_mode(usuario_label, senha_label, login_button, resultado_label, dark_button)

def set_dark_mode(usuario_label, senha_label, login_button, resultado_label, dark_button):
    janela.config(bg="#4c6199")
    usuario_label.config(bg="#4c6199", fg="white")
    senha_label.config(bg="#4c6199", fg="white")
    login_button.config(bg="#291e4c", fg="white")
    resultado_label.config(bg="#4c6199", fg="white")
    dark_button.config(text="Light Mode")

def set_light_mode(usuario_label, senha_label, login_button, resultado_label, dark_button):
    janela.config(bg="#80a2ff")
    usuario_label.config(bg="#80a2ff", fg="black")
    senha_label.config(bg="#80a2ff", fg="black")
    login_button.config(bg="#8b67ff", fg="black")
    resultado_label.config(bg="#80a2ff", fg="black")
    dark_button.config(text="Dark Mode")

def verificar_login():
    usuario = usuario_inserido.get()
    senha = senha_inserido.get()

    if usuario == "1" and senha == "1":
        resultado_label.config(foreground="green", text="Login bem-sucedido!")
    else:
        resultado_label.config(foreground="red", text="Erro, verifique seu usuário e senha.")

# Janela Padrão
janela = tk.Tk()
janela.title("Painel de Login")
janela.geometry("400x120")
fonte = ("arial", 12)
set_light_mode()  # Iniciar com o modo claro

# Labels
usuario_label = tk.Label(janela, text="Usuário:", width=13, font=fonte)
usuario_label.pack()
senha_label = tk.Label(janela, text="Senha:", width=13, font=fonte)
senha_label.pack()
resultado_label = tk.Label(janela, text="", width=31, font=fonte)
resultado_label.pack()

# Inputs
usuario_inserido = tk.Entry(janela, width=25)
senha_inserido = tk.Entry(janela, show="*", width=25)

# Botões
login_button = tk.Button(janela, text="Acessar", width=10, command=verificar_login)
dark_button = tk.Button(janela, text="Dark Mode", width=10, command=toggle_dark_mode)

# Organiza os widgets na janela
usuario_label.place(x=0, y=10)
senha_label.place(x=0, y=40)
usuario_inserido.place(x=100, y=10)
senha_inserido.place(x=100, y=40)
login_button.place(x=20, y=80)
resultado_label.place(x=100, y=80)
dark_button.place(x=300, y=10)

# Inicializa a janela principal
janela.mainloop()
