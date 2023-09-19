#bibliotecas 

import os 
from time import sleep
from getpass import getpass
import stdiomask

#Inicio

#Painel de Login e Cadastro
i = True
def menu():
    print("Sistema de Login")
    print("Escolha uma opcao")
    print("[1] Cadastras um novo Usuario (Nao feito)")
    print("[2] Fazer login")
    print("[3] Sair (nao feito)")
    chosen = int(input('Digite sua opcao: '))
    while chosen > 3 or chosen < 1: 
        os.system('cls')
        print("opcao nao encontrado!!")
        print("[1] Cadastras um novo Usuario (Nao feito)")
        print("[2] Fazer login")
        print("[3] Sair (nao feito)")
        chosen = int(input('Digite sua opcao: '))
    return(chosen)
    
    
def fazer_login():
    user = input("User: ")
    pasw = stdiomask.getpass(prompt="Password: ",mask=" ")
    return(user, pasw)
    
    
    
for i in range (1):
    os.system('cls')
    chosen = menu()
    
    if chosen == 1: 
    
        #cadastrar novo usuario 
        print("cadastrando")
        
    elif chosen == 2:
        #login 
        print("Login")
        
    elif chosen == 3:
        print("saindo")
        break