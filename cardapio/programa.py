from funcao import *

print( ''' Menu:
        1- Ver cardápio
        2- Adicionar item ao pedido
        3- Ver pedido
        4- Remover item
        0- Finalizar ''' )

listacardapio = []

while True:
    op = input("o que deseja fazer:")

    if op == "1":
        print(carregar_cardapio(listacardapio))
        print(exibir_cardapio(listacardapio))