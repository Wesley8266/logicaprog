#questao 1
# lista =[]
# cont = 0
# for i in range(5):
#     nome = input(f"digite o {i + 1}° nome: ")
#     lista.append(nome)
# for a in lista:
#     if a[0] != "a" and a[0] != "A":
#         cont += 1
# print(f"nomes digitados: {lista}")
# print(f"{cont} nomes não começam com A")

#questao 2
soma = 0
divisao = 0
notas = input("quantidade de notas do aluno: ")
def calcular_media():
    for i in range(notas):
        n = float(input(f"digite a {i + 1}° nota: "))
    soma += n
    divisão += notas
    media = soma / divisao
    if media >= 7:
        print(f"{media}: aprovado")
    else:
        print(f"{media}: reprovado")
        
calcular_media()