import os 
tarefas = []

os.system('cls')
print("bem Vindo a sua lista de tarefas!")
input("Pressione qualquer tecla para continuar...")

while True:
    os.system('cls')
    print("Essa são suas tarefas atuais.")
    print("=========================")
    for a in range (0,len(tarefas)): 
        print(a,"-",tarefas[a])
    print("=========================")    
    input("Pressione qualquer tecla para continuar...")
    print(" 1- Incluir tarefa","\n","2- Marcar como Feita","\n","3- Remover uma tarefa","\n","4- Esvaziar a lista")
    choosen=int(input("O que deseja fazer? ",))

    if choosen == 1:
        os.system('cls')
        tarefas.append(input("Digite sua tarefa:"))

    if choosen == 2:
        os.system('cls')
        print("=========================")
        for a in range (0,len(tarefas)): 
            print(a,"-",tarefas[a])
        print("=========================")
        i=int(input("qual tarefa você concluiu?"))
        backup = tarefas[i] +" concluida 👍"
        tarefas[a]=backup
    
    if choosen == 3: 
        os.system('cls')
        print("=========================")
        for a in range (0,len(tarefas)): 
            print(a,"-",tarefas[a])
        print("=========================")
        tarefas.pop(int(input('Qual tarefa você deseja remover?')))

    if choosen == 4: 
        os.system('cls')
        tarefas.clear()
    