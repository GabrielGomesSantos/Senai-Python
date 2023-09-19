import json
contato=[]

x=input("Nome: ")
y=input("senha: ")

contato={
    "nome": x,
    "telefone":y
    }

for item in contato:
   for chaves, valores in item.items():
      print("chaves", valores)
      print("Valores:", valores)

saida = json.dumps(contato)

contato2 = json.loads(saida)

for item in contato2:
    for chaves, valores in item.items():
        print("chave: ", chaves)
        print("Valor:",valores)

contato.append(contato)

with open("file.json", 'a') as file:
    json.dump(contato, file, indent=4)
print("Cadastro feito!")    

# with open('file_2.json', 'w') as json_file:
#   json.dump(contato, json_file, indent=4)

