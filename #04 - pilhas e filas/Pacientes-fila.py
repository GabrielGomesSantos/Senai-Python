import random as r 
fila = {}
lista = [1, 2, 3, 4, 5]
sala =  r.choice(lista)

class Paciente: 
    
    def atributos():
      nome = input("Nome do paciente:")
      numero = (len(fila)+1)
      dados = [nome, numero]
      return(dados)
      
class Filadeatendimento: 
    
    def registro():
        paciente = Paciente
        fila.apended(paciente)
    
    def chamar():
        fila.pop()
        print(fila[0],"Doutor esta o chamando na sala",sala) 