import agenda as a
import os
os.system('cls')
print("")
print("bem-Vindo a sua agenda de contatos!")
print("")

while True: 
    os.system('cls')
    print("=========================")
    print("1 - Adicionar um contato")
    print("2 - Editar um contato")
    print("3 - Lista de contatos")
    print("4 - Excluir um contato")
    print("5 - Limpar Agenda")
    print("=========================")
    choosen = int(input("O que deseja fazer:"))
    
    match choosen:
        
        case 1: 
            a.add()
            
        case 2:
            a.edit()
            
        case 3: 
            a.lis()
        
        case 4: 
            a.excl()
        
        case 5:
            a.clean()            