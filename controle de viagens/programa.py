from funcoes import*


print("1 - Registrar nova viagem-----------------------------------")
print("2 - Exibir todas as viagens")
print("3 - Buscar viagens por motorista")
print("4 - Exibir viagem mais cara ")
print("5 - Mostrar média geral de consumo ")
print("0 - Sair-------------------------------")

listaviagens=[]
while True:
    opcao = int(input("o que deseja fazer? "))
    
    if opcao == 1:
        registrar_viagens(listaviagens)
    elif opcao == 2:
        print(exibir_viagens(listaviagens))
    elif opcao == 3: 
        print(buscar_motorista(listaviagens))
    elif opcao == 4:
        print(viagem_mais_cara(listaviagens))
    elif opcao ==5:
        print(media_consumo(listaviagens))
    elif opcao == 0:
        print("programa encerrado.......")
        break
    
