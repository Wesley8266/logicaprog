from tabulate import tabulate


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
    tabela = []
    for i in listaviagens:
        tabela.append([i["motorista"], i["destino"], i["distancia"], i["gasto_combustivel"], i["consumo"]])
    print(tabulate(
        tabela, 
        headers= ["motorista","destino","distancia","gasto_combustivel","consumo"], tablefmt = "fancy_grid"))



def buscar_motorista(listaviagens):
    viagem_m = []
    motorista = input("qual motorista deseja consultar: ")
    for i in listaviagens:
        if motorista == i["motorista"]:
            viagem_m.append(i)
    print(tabulate([viagem_m], headers = "keys", tablefmt = "fancy_grid"))


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
        distancia += viagem["distancia"]
    media = total / distancia
    print(f"consumo:{media}")
        