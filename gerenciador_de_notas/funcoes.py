def calcular_media(ListaNotas):
    media = sum(ListaNotas) / len (ListaNotas)
    return media

def verificar_situacao(media):
    if media >= 7:
        return "aprovado"
    elif media >= 5 and media < 7:
        return "recuperação"
    else:
        return "Reprovado" 