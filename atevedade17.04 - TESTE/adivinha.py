#1
print("Hello, World!")

#2
idade = int(input("Digite sua idade: "))
if idade >= 16:
    print("Você pode votar.")
else:
    print("Você não pode votar.")

#3
total = 0.0
while True:
    numero = float(input("Digite um número (0 para sair): "))
    if numero == 0:
        break
    total += numero
print("o total das compras é:", total)

#4
def calcular_imc():
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em metros: "))
    imc = peso / (altura ** 2)
    if imc < 18.5:
        print("Você está abaixo do peso.")
    elif imc < 25:
        print("Você está com o peso normal.")
    elif imc < 30:
        print("Você está acima do peso.")
    else:
        print("Você está obeso.")

#5
amigos = ["Alice", "Bob", "Charlie", "David", "Eve"]
quantidade = int(input("Quantos amigos você tem? "))
if quantidade > len(amigos):
    if quantidade % 2 == 0:
        print("quantidade par!")
    else:
        print("quantidade ímpar!")

#6
temperatura = []
for i in range(7):
    temp = float(input(f"Digite a temperatura do dia {i+1}: "))
    temperatura.append(temp)
media = sum(temperatura) / len(temperatura)
print(f"A temperatura média é: {media:.2f}°C")

#7
vendas = [100, 150, 200, 250, 300]
soma = 0
for v in vendas:
    if v % 2 == 0:
        soma += v

print("A soma dos valores de vendas pares é:", soma)

#8
valor = float(input("Digite um valor total: "))
if valor > 500:
    desconto = valor * 0.2
elif valor >= 200:
    desconto = valor * 0.1
else:
    desconto = 0
valor_com_desconto = valor - desconto
print(f"Valor com desconto: {valor_com_desconto:.2f}")

#9
notas = [5, 6, 7, 8, 9, 10]
contador = 0
for nota in notas:
    if nota >= 7:
        contador += 1
print("Quantidade de notas acima de 7:", contador)

#10
frase = input("Digite uma frase: ").lower()
vogais = "aeiou"
contador_vogais = 0
for letra in frase:
    if letra in vogais:
        contador_vogais += 1
print("Quantidade de vogais na frase:", contador_vogais)

#11
idades =[]

for i in range(5):
    idade = int(input("digite uma idade:"))
    idades.append(idade)

idades.sort()
print("A soma é:", idades)    

#12
while True:
    print("\n1-soma\n2-subtração\n3-multiplicação\n4-divisão\n5-sair")
    escolha = int(input("Escolha uma operação: "))  
    if escolha == 5:
        print("Saindo...")
        break   

try:
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))

if escolha == "1":
    print("Resultado:", a + b)
elif escolha == "2":
    print("Resultado:", a - b)
elif escolha == "3":
    print("Resultado:", a * b)
elif escolha == "4":
    if b != 0:
        print("Resultado:", a / b)
else:
    print("Erro: Divisão por zero não é permitida.")   

except ValueError:
    print("Erro: Entrada inválida. Por favor, digite um número.")