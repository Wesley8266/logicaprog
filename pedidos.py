def novo_pedido(cardapio):
    pedido = {}
    item = input("id do item: ")
    for i in cardapio:
        if item == i["id"]:
            preco = i["preco"]
            quantidade = int(input("quantidade: "))
            subtotal = preco * quantidade
            pedido.append(i)
            total = {
                "id": 1,
                "item": i["id"],
                "quantidade": quantidade,
                "total": subtotal
            }
        return pedido
