# peso = float(input("insira o peso: "))
# altura = float(input("insira a sua altura em metros: "))
# imc = peso / (altura ** 2)
# if imc < 18.5:
#     print(f"{imc} abaixo do peso")
# elif imc <= 24.9:
#     print(f"{imc} peso normal")
# elif imc <= 29.9:
#     print(f"{imc} sobrepeso")
# else :
#     print(f"{imc} obeso")


# n = int(input("insira um numero inteiro: "))
# for i in range(n + 1):
#     if i % 2 == 0:
#         print(f"{i} é par")
#     else :
#         print(f"{i} é impar")

# Numero = int(input("insira o número: "))
# for i in range (1,11):
#    resultado = Numero * i
#    print(f"Número: {Numero} * {i} = {resultado} ")

# n = int(input("digite um numero inteiro: "))
# if n % 1:
#     print("esse numero é primo")
# elif n % n:
#     print("esse numero é primo")
# else:
#     print("esse numero nao é primo")

alu = int(input("quantos alunos tem na sua turma? "))
aluno = 0
notas = 0
for n in range(alu):
    while True:
        no = float(input(f"digite a nota do aluno {n +1}:"))
        break


