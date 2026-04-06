import random

numero = random.randint(1, 100)
palpite = 0
tentativas = 0

while palpite != numero:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

    if palpite != numero:
        print("maior" if palpite < numero else "menor")

print(f"Você acertou! Total de tentativas: {tentativas}")

numeros = [int(input(f"Digite o {i+1}º número: ")) for i in range(8)]

print("Números repetidos:")

ja_mostrados = []

for n in numeros:
    if numeros.count(n) > 1 and n not in ja_mostrados:
        print(f"{n} apareceu {numeros.count(n)} vezes")
        ja_mostrados.append(n)
        
