import json

def escrever_json(lista):
    with open('meu_arquivo.json', 'w', encoding='utf-8') as f:
        for nome in lista:
            f.write(nome + '\n')


minha_lista = ['João', 'Maria', 'José','gabriel']
escrever_json(minha_lista)

def carregar_json():
    with open('meu_arquivo.json', 'r', encoding='utf-8') as f:
        return [nome.strip() for nome in f.readlines()]
    
print(carregar_json())  # ['João\n', 'Maria\n', 'José\n']