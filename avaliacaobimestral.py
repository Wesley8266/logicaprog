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

# questão 2(media de notas)
# def calcular_media(lista_notas):
#     soma = 0
#     quantidade = 0
#     for nota in lista_notas:
#         soma += nota
#         quantidade += 1
#     return soma / quantidade
# notas = []
# for i in range(4):
#     nota = float(input(f"Digite a {i+1} nota: "))
#     notas.append(nota)
# media = calcular_media(notas)
# print(f"Média = {media}")
# if media >= 7:
#     print("Aluno aprovado!")
# else:
#     print("Aluno reprovado!")

#questao 3
# impar = 0
# par = 0
# for i in range(10):
#     n = int(input(f"digite o {i + 1}º numero: "))
#     if n % 2 == 0:
#         par += 1
#     else:
#         impar += 1
# print(f"a quantidade de numero pares é {par}")
# print(f"a quantidade de numero impares é {impar}")

# questao 4 (lista de convidados)
# nomes = []
# for i in range(5):
#     no = input(f"Digite o {i+1} nome: ")
#     nomes.append(no)
# busca = input("Digite o nome que deseja procurar: ")
# encontrado = False
# for i in range(len(nomes)):
#     if nomes[i] == busca:
#         encontrado = True
#         break
# if encontrado:
#     print(f"convidado {busca} encontrado(a) na lista!")
# else:
#     print("convidado não encontrado na lista.")

#questao 5
# def filtrar_nomes(nomes):
#     return [nome for nome in nomes if len(nome) > 5]

# nomes_usuario = []
# for i in range(7):
#     nome = input(f"Digite o nome {i+1}: ")
#     nomes_usuario.append(nome)

# nomes_filtrados = filtrar_nomes(nomes_usuario)
# print("Nomes com mais de 5 letras:", nomes_filtrados)

#questao 6
# numeros = []
# for i in range(6):
#     num = int(input(f"Digite o número {i+1}: "))
#     numeros.append(num)

# posicao = int(input("Digite uma posição (índice): "))

# if 0 <= posicao < len(numeros):
#     print(f"O número na posição {posicao} é {numeros[posicao]}")
# else:
#     print("Posição inválida!")

#questao 7
# def par_ou_impar(numero):
#     if numero % 2 == 0:
#         return "Par"
#     else:
#         return "Ímpar"

# num = int(input("Digite um número inteiro: "))
# resultado = par_ou_impar(num)
# print(f"O número {num} é {resultado}.")

#questao 8
# contador = 10
# for i in range(10,-1,-1):
#     print(i)
#     contador - 1
# print("EXPLODIUUUUUUUUUU")