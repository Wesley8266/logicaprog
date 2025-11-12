
def registrar_viagens(listaviagens):
    motorista = input("nome do motorista:")
    destino = input("destino: ")
    distancia = float(input("distancia em km: "))
    gasto_combustivel  =float(input( "Valor gasto com combustível(em R$):"))
    consumo = gasto_combustivel / distancia
    viagem = {"motorista": motorista, "destino": destino, "distancia":distancia, "gasto_combustivel": gasto_combustivel, "consumo": consumo}
    listaviagens.append(viagem)
    return viagem

def exibir_viagens(listaviagens):
    return listaviagens


def buscar_motorista(listaviagens):
    motorista = input("qual motorista deseja consultar: ")
    viagens_m = []
    for i in listaviagens:
        if motorista == i["motorista"]:
            viagens_m.append(i)
            return print(viagens_m) 
        elif motorista != ["motorista"]:
            return print("motorista nao encontrado")


def viagem_mais_cara(listaviagens):
    maior = 0
    for i in listaviagens:
        if i["gasto_combustivel"] >= maior:
           maior = i["gasto_combustivel"]
    return maior


def media_consumo(listaviagens):
    total = 0
    distancia = 0
    for viagem in listaviagens:
        total += viagem["gasto_combustivel"]
        total_distancia += viagem["distancia"]
    media = total / distancia
    return media
        