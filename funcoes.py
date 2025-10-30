def adicionarlivro(listalivros):
    titulo=input("Digite o título do  livro: ")
    autor=input("Digite o autor do livro: ")
    status="Disponível"
    livro={"titulo": titulo, "autor": autor, "status": status}
    listalivros.append(livro)
    return listalivros

def exibirlivros(listalivros):
    return listalivros

def emprestarlivro(listalivros):
    livro = input("qual livro deseja emprestar: ")
    for i in listalivros:
         if livro == i["titulo"]:
             i["status"]="emprestado"
    return listalivros

def devolverlivro(listalivros):
    livro = input("qual livro deseja devolver: ")
    for i in listalivros:
         if livro == i["titulo"]:
             i["status"]="disponivel"
    return listalivros


