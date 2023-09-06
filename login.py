import os
from time import sleep
os.system("cls")

for i in range(1, 4):
        
    user=input("User: ")
    sleep(0.5)
    pasw=input("Password: ")
    sleep(0.5)
    os.system("cls")

    if user == "admin" and pasw == "1234":
        print('Bem vindo ',user)
        sleep(2)
        break

    else:
        print("Nome de usuario ou senha Incorretos!")
        sleep(2)
        os.system("cls")
