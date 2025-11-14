from operações import *

print("1-soma")
print("2-subtraçao")
print("3-multiplicaçao")
print("4-divisao")
print("0-sair")


while True:
    a = float(input("digite o 1° numero: "))
    operacao= input("escolha a operaçao: ")
    b = float(input("digite o 2° numero: "))
    
    if operacao == "1":
        print(soma(a,b))
    elif operacao == "2":
        print(subtracao(a,b))
    elif operacao == "3":
        print(multiplicacao(a,b))
    elif operacao == "4":
        print(divisao(a,b))
    elif operacao == "0":
        print("programa encerrado! ")
        break


