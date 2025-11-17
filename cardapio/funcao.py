from tabulate import tabulate
def carregar_cardapio(listacardapio):
    lista = [
        {"id": "1", "nome": "Hambúrguer", "preco": 12.5},
        {"id": "2", "nome": "Pizza", "preco": 30},
        {"id": "3", "nome": "Refrigerante", "preco": 5}
    ]
    listacardapio.append(lista)
    return listacardapio

def exibir_cardapio(lista):
    tabela = []
    for i in lista:
        tabela.append([i["id"], i["nome"], i["preco"]])
    print(tabulate(
        tabela, 
        headers= ["id","produto","preço"], tablefmt = "fancy_grid"))



def adicionar_pedido(listacardapio):
    total=0
    listapedido = []
    adicionar = input("qual id do ítem? ")
    for i in listacardapio:
        if adicionar == i["id"]:
            qua=int(input("Qual será a quantidade? "))
            total= i["id"] * qua
        pedido={
            "item":adicionar,
            "quantidade":qua,
            "total":total
        }
        listapedido.append()
        return listapedido


def remover_pedido(listapedido):
    re=input("Qual pedido deseja remover? ")
    for i in listapedido:
        if re==i["id"]:
            listapedido.remove(re)



