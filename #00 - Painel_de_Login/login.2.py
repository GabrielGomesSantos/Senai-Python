import mysql.connector
import tkinter as tk
from tkinter import messagebox

# Configurações do banco de dados
DB_HOST = "localhost"
DB_USER = "seu_usuario"
DB_PASSWORD = "sua_senha"
DB_DATABASE = "minha_base_de_dados"

# Função para criar a tabela de usuários (chamada apenas uma vez)
def criar_tabela_usuarios():
    connection = mysql.connector.connect(
        host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_DATABASE
    )
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            usuario VARCHAR(255) NOT NULL,
            senha VARCHAR(255) NOT NULL
        )
        """
    )
    connection.commit()
    connection.close()

# Função para fazer login
def fazer_login():
    user = entry_user.get()
    pasw = entry_password.get()
    
    connection = mysql.connector.connect(
        host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_DATABASE
    )
    cursor = connection.cursor()
    
    cursor.execute(
        "SELECT * FROM usuarios WHERE usuario = %s AND senha = %s",
        (user, pasw)
    )
    
    if cursor.fetchone():
        messagebox.showinfo("Login", "Login bem-sucedido!")
    else:
        messagebox.showerror("Login", "Usuário ou senha incorretos.")
    
    connection.close()

# Função para fazer cadastro
def fazer_cadastro():
    user = entry_user_cadastro.get()
    pasw = entry_password_cadastro.get()
    
    connection = mysql.connector.connect(
        host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_DATABASE
    )
    cursor = connection.cursor()
    
    cursor.execute(
        "INSERT INTO usuarios (usuario, senha) VALUES (%s, %s)",
        (user, pasw)
    )
    
    connection.commit()
    connection.close()
    
    messagebox.showinfo("Cadastro", "Cadastro realizado com sucesso!")

# Restante do código permanece igual
