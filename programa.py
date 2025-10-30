from funcoes import *

print("1 - Adicionar livro-----------------------------------")
print("2 - Exibir todos os livros")
print("3 - Emprestar livro")
print("4 - Devolver livro")
print("0 - Sair-------------------------------")

listalivros = []
while True:
    opcao = int(input("o que deseja fazer? "))
    if opcao == 1:
        adicionarlivro(listalivros)
    elif opcao == 2:
        print(exibirlivros(listalivros))
    elif opcao == 3: 
        print(emprestarlivro(listalivros))
    elif opcao == 4:
        print(devolverlivro(listalivros))
    elif opcao == 0:
        print("programa encerrado.......")
        break