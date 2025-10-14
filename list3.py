#01
# altura = float(input("diga-me seu altura"))
# peso = float(input("diga-me agora o seu peso"))
# imc = peso / (altura * altura )
# if imc < 18.5:
#     print("abaixo do peso")
# elif imc >= 18.5:
#     print("peso normal")
# elif imc < 25.0:
#     print("peso normal")
# elif imc >= 25:
#     print("sobrepeso")
# elif imc <= 29.9:
#     print("sobrepeso")
# elif imc > 30:
#     print("obesidade")

#02
# N = int(input("Por favor, insira um número inteiro N: "))
# for numero in range(1, N + 1):
#     if numero % 2 == 0:
#         print(f"{numero} : par")
#     else:
#         print(f"{numero} : ímpar")
     
#03
# num = int(input("Digite um número inteiro para gerar a tabuada: "))

# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")

# #04
# def eh_primo(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# num = int(input("Digite um número inteiro para verificar se é primo: "))

# if eh_primo(num):
#     print(f"{num} é primo.")
# else:
#     print(f"{num} não é primo.")

# #05
# qtd_alunos = int(input("Digite a quantidade de alunos da turma: "))
# notas = []

# for i in range(qtd_alunos):
#     nota = float(input(f"Digite a nota do aluno {i+1}: "))
#     notas.append(nota)

# media_geral = sum(notas) / qtd_alunos
# acima = len([nota for nota in notas if nota > media_geral])
# abaixo = len([nota for nota in notas if nota < media_geral])

# print(f"Média geral: {media_geral:.2f}")
# print(f"Alunos acima da média: {acima}")
# print(f"Alunos abaixo da média: {abaixo}")

# #06
# import random

# numero_secreto = random.randint(1, 20)
# tentativa = None

# print("Tente adivinhar o número secreto entre 1 e 20!")

# while tentativa != numero_secreto:
#     tentativa = int(input("Digite seu palpite: "))
#     if tentativa < numero_secreto:
#         print("O número secreto é maior.")
#     elif tentativa > numero_secreto:
#         print("O número secreto é menor.")
#     else:
#         print("Parabéns! Você acertou.")