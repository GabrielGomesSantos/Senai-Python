import os
agenda = []

def add():
    os.system('cls')
    nome=input("Digite o nome do seu contato:")
    telefone=(input("Digite o numero de :"))
    contato = [nome,telefone]

    agenda.append(contato)
    print("Contato adicionado com sucesso")

def edit():
    os.system('cls')
    print("=========================")
    for i in range(0,len(agenda)):
        print(i+1,"-",agenda[i][0], agenda[i][1])
    print("=========================")
    e=int(input("qual contato você deseja alterar: "))
    e=e-1
    os.system('cls')
    print(agenda[e][0], agenda[e][1])
    e1=int(input("qual parte você deseja alterar?\n1-Nome\n2-Telefone\n"))
    match e1:
        case 1: 
            agenda[e][0] = input("Digite o novo nome do seu contato:")

        case 2:
            agenda[e][1] = int(input("Digite o novo numero do seu contato:"))
        case _:
            print("Opção nao encontrato")
            e1=int(input("qual parte você deseja alterar?\n1-Nome\n2-Telefone"))
        
    
def lis():
    os.system('cls')
    print("=========================")
    for i in range(0,len(agenda)):
        print(i+1,"-","Nome:",agenda[i][0],"telefone:", agenda[i][1])
    print("=========================")
    input("Precione qualquer tecla para continuar...")

def excl():
    os.system('cls')
    print("=========================")
    for i in range(0,len(agenda)):
        print(i+1,"-",agenda[i][0], agenda[i][1])
    print("=========================")     
    a=int(input('Qual contato você deseja remover?'))
    agenda.pop(a-1)
    print("Contato removido com sucesso!")
    
def clean():
    os.system('cls')
    agenda.clear()
 
