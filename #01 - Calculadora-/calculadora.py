##bibliotecas
import os
import math
from time import sleep


def menu():
    os.system('cls')
    print("=============================")
    print("[1] - Soma")
    print("[2] - Subtração")
    print("[3] - Multiplicação")
    print("[4] - Divisão")
    print("[5] - Potenciação")
    print("[6] - Radiciação")
    print("=============================")
    choosen = int(input("Digite o númeroo da opção:"))
    return(choosen)



def soma():
    a=int(input("Valor 1:"))
    b=int(input("Valor 2:"))    
    return(a+b)

def sub():
    a=int(input("Valor 1:"))
    b=int(input("Valor 2:"))  
    return(a-b)

def mult():
    a=int(input("Valor 1:"))
    b=int(input("Valor 2:"))  
    return(a*b)

def div():
    a=int(input("Valor 1:"))
    b=int(input("Valor 2:")) 
    if b != 0:
        return(a/b)
    else:
        print("Impossivel dividir por 0")
        

def poten(): 
    a=int(input("Valor 1:"))
    b=int(input("Valor 2:"))   
    return(math.pow(a, b))
    
def rad():     
    a=int(input("Valor 1:"))
    b=int(input("Valor 2:"))   
    return(math.pow(a, 1/b)) 

#Inicio
while True:
    os.system('cls')
    print("Loadding.")
    sleep(0.5)
    os.system('cls')
    print("Loadding..")
    sleep(0.5)
    os.system('cls')
    print("Loadding...")
    sleep(0.5)
    os.system('cls')
    choice=menu()

    match choice:
        
        case 1:            
            print(soma())
            input("presione qualquer tecla para calcular dnv...")
        
        case 2:              
            print(sub())
            input("presione qualquer tecla para calcular dnv...")
            
        case 3:            
            print(mult())
            input("presione qualquer tecla para calcular dnv...")

        case 4:             
            print(div())
            input("presione qualquer tecla para calcular dnv...")

        case 5:           
            print(poten())
            input("presione qualquer tecla para calcular dnv...")
        
        case 6:              
            print(rad())
            input("presione qualquer tecla para calcular dnv...")

        case _: 
            print("Operaçao Invalida!")   
            input("presione qualquer tecla para calcular dnv...")