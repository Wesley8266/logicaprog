def registrar_viagens(listaviagens):
    motorista = input("nome do motorista:")
    destino = input("destino: ")
    distancia = float(input("distancia em km: "))
    gasto_combustivel  =float(input( "Valor gasto com combustível(em R$):"))
    consumo = gasto_combustivel / distancia
    viagem = {"motorista": motorista, "destino": destino, "distancia":distancia, "gasto": gasto_combustivel, "consumo": consumo}
    listaviagens.append(viagem)
    return viagem

def exibir_viagens(listaviagens):
    return listaviagens

def buscar_motorista(listaviagens):
    motorista = input("qual motorista deseja consultar: ")
    for i in listaviagens:
        if motorista != i["motorista"]:
            return "motorista nao encontrado!"
        elif motorista == i["motorista"]:
            return motorista

def viagem_mais_cara(listaviagens):
    for i in listaviagens:
        maior_valor = max["gasto"]
        print(f"a viagem com maior valor é {maior_valor}")


def media_consumo(listaviagem):
    for i in listaviagem:
        media = ["gasto"] / ["distancia"]
    return media
        