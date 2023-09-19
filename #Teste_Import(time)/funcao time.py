from datetime import datetime
hora = datetime.now().hour

def saud(nome):
    if hora>= 0 and hora <=12:
        print("Bom Dia!",nome)
    elif hora>17:
        print("Boa Noite!",nome)
    else:
        print("Boa Tarde",nome)

saud("gabriel")