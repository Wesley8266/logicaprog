from tabulate import tabulate


def carregar_cardapio(listacardapio):
    lista = [{"id": 1, "nome": "Hambúrguer", "preco": 12.5}, {"id": 2, "nome": "Pizza", "preco": 30}, {"id": 3, "nome": "Refrigerante", "preco": 5}]
    listacardapio.append(lista)
    return listacardapio

def exibir_cardapio(listacardapio):
    print(tabulate(
        listacardapio, 
        headers="keys"))



def adicionar_pedido(listacardapio):
    pedido = []
    item = input("id: ")

def exibir_pedido(pedido):
    return pedido


def remover_pedido(listapedido):
    re=input("Qual pedido deseja remover? ")
    for i in listapedido:
        if re==i["id"]:
            listapedido.remove(re)



