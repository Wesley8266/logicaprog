import emoji 

def soma(a,b):
     return emoji.emojize(f"{a + b}:thumbs_up:")
     
def subtracao(a,b):
     return emoji.emojize(f"{a - b}:thumbs_up:")
     
def multiplicacao(a,b):
     return emoji.emojize(f"{a * b}:thumbs_up:")
     
def divisao(a,b):
     if b == 0:
        print("não é possivel dividir por 0")
     else:
        return emoji.emojize(f"{a / b}:thumbs_up:")
