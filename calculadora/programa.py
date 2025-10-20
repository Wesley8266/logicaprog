from operacoes import *
import emoji
print("1-soma")
print("2-subtraçao")
print("3-multiplicaçao")
print("4-divisao")
print("0-sair")
a = float(input("digite o 1° numero: "))
b = float(input("digite o 2° numero: "))

while True:
    operacao= input("escolha a operaçao: ")
    if operacao == "1":
        print(soma(a,b))
    elif operacao == "2":
        print(subtraçao(a,b))
    elif operacao == "3":
        print(multiplicacao(a,b))
    elif operacao == "4":
        print(divisao(a,b))
    elif operacao == "0":
        print(f"programa encerrado {emoji} ")
        break
emoji = emoji.emojize(":OK_hand:")