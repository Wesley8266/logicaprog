from funcoes import *

ListaNotas = []
notaDict = {}

print("insira 1 para cadatrar aluno")
print("insira 2 para exibir relatório de aluno")
print("insira 0 para sair do programa")

while True:
    opcao = input("qual procedimento deseja realizar? ")
    if opcao == "1":
        print("cadastro: ")
        nome = input("nome do aluno: ")

        for i in range(3):
            notas = float(input("notas do aluno: "))
            ListaNotas.append(notas)
    elif opcao == "2":
        print(f"nome do aluno: {nome}")
        print(f"Notas: {ListaNotas}")
        print(f"media: {calcular_media(ListaNotas)}")
        print(f"situaçao: {verificar_situacao(calcular_media)}")
        
    

