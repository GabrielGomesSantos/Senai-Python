import tkinter as tk

# Dados de login fictícios
dados_de_login = {"usuario1": "senha1", "usuario2": "senha2"}

# Função para verificar o login
def verificar_login():
  usuario = usuario_entry.get()
  senha = senha_entry.get()

  if usuario in dados_de_login and dados_de_login[usuario] == senha:
    resultado_label.config(text="Login bem-sucedido!")
  else:
    resultado_label.config(text="Login falhou. Verifique seu usuário e senha.")

#fonte
fonte = ("arial", 15)
# Cria uma janela principal
janela = tk.Tk()
janela.title("Sistema de Login")

# Cria rótulos
usuario_label = tk.Label(janela, text="Usuário:", font=fonte)
senha_label = tk.Label(janela, text="Senha:", font=fonte)
resultado_label = tk.Label(janela, text="", font=fonte)

# Cria campos de entrada
usuario_entry = tk.Entry(janela)
senha_entry = tk.Entry(janela, show="*") # A senha será exibida como asteriscos

# Cria um botão de login
login_button = tk.Button(janela, text="Acessar!", command=verificar_login, font=fonte)

# Organiza os widgets na janela
usuario_label.grid(row=0, column=0)
senha_label.grid(row=1, column=0)
usuario_entry.grid(row=0, column=1)
senha_entry.grid(row=1, column=1)
login_button.grid(row=2, columnspan=2)
resultado_label.grid(row=3, columnspan=2)

# Inicializa a janela
janela.mainloop()