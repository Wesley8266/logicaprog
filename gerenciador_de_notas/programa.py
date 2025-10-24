from funcoes import *

ListaNotas = []
print("insira 1 para cadatrar aluno")
print("insira 2 para exibir relatório de aluno")
print("insira 0 para sair do programa")
print("insira 3 para cadastrar um novo aluno")
while True:
    opcao = input("qual procedimento deseja realizar? ")
    if opcao == "1":
        print("cadastro: ")
        nome = input("nome do aluno: ")

        listadict = {"NOME" : nome}
        for i in range(3):
            notas = float(input("notas do aluno: "))
            ListaNotas.append(notas)
            media = calcular_media(ListaNotas)
    
    elif opcao == "2":
        print(f"nome do aluno: {nome}")
        print(f"Notas: {ListaNotas}")
        print(f"media: {calcular_media(ListaNotas)}")
        print(f"situaçao: {verificar_situacao(media)}")

    elif opcao == "0":
        print("programa encerrado!")
        break


        
    

