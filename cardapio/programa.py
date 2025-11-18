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
        listacardapio = carregar_cardapio(listacardapio)
        exibir_cardapio(listacardapio)
    if op == "2":
        adicionar_pedido(listacardapio)
    if op == "3":
        exibir_pedido(listacardapio)