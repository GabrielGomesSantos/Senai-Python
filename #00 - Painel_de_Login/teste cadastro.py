import json
cadastro=[]

user = input("User: ")
pasw = input("Password: ")

dados={
    "User:",user,
    "password:",pasw
    }

cadastro.append(dados)

with open("cadastro_new.json", 'a') as file: 
    json.dump(cadastro, file, indent=5)
print("Cadastro realizado com sucesso!!")
