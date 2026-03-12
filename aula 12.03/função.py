print("pythin e facil")
print("pythin e facil")
print("pythin e facil")

def exibirMensagem():
    print("pythin e facil")

exibirMensagem()

def saudar(nome):
    print(f"ola, {nome}")

saudar("ana")
saudar("bruna") 

def exibirMensagem(nome, mensagem):
    print(f"{mensagem}, {nome}")

exibirMensagem("ana", "bom dia") 

exibirMensagem(nome ="bruno", mensagem = "boa noite")

def calcularMedia(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media

resultado = calcularMedia(8.0, 9.0)
print(f"media: {resultado}")