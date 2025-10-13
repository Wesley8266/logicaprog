import requests 
dados = requests.get(f"https://api.apyhub.com/data/dictionary/timezone")
print(dados.json())
