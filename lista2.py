# soma = 0
# for i in range (3):
#     notas = int(input('diga suas notas: '))
#     soma += notas
# med = soma / 3
# if med >= 7:
#     print(f'{med} aprovado, parabens')
# else:
#     print(f'{med} reprovado, que pena')


# cont = 0
# vogal = ['A', 'E', 'I', 'O', 'U']
# palavra = input("digite uma palavra: ").upper()
# for letra in palavra:
#     if letra in vogal:
#         cont += 1
# print(f"a palavra tem {cont} vogais!")


# n =int(input("digite o numero: "))
# if n % 2 == 0 :
#     print("o numero é par")
# else:
#    print("Numero é impar")

# for i in range(5):
#     N = int(input("digite os numeros: "))
#     if i == 0 :
#         maior = menor = N
#     elif N > maior:
#         maior = N
#     elif N < menor:
#         menor = N
# print(f"o maior valor é {maior} e o menor é {menor}")

cont = total = 0
while True :
    a= float(input("digite o valor dos produtos: "))
    total += a
    if a == 0 :
        print("programa encerrado")
        break
    elif a >= 100:
        cont += 1

    
    