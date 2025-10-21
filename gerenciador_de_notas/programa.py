from funcoes import *

ListaNotas = []
print("insira 1 para cadatrar aluno")
print("insira 2 para exibir relatório de aluno")
print("insira 0 para sair do programa")
while True:
    opcao = input("qual procedimento deseja realizar? ")
    if opcao == "1":
        print("cadastro")
        nome = input("nome do aluno: ")
        for i in range(3):
            notas = int(input("notas do aluno: "))
            ListaNotas.append(notas)
    elif opcao == "2":
        print(f"nome do aluno: {nome}")
        print(f"Notas: {ListaNotas}")
        print("media:", Lista_Notas(ListaNotas))


        
    

