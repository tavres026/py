print("ola, mundo!")

print("ola, mundo!")
print("ola, mundo!")
print("ola, mundo!")

cont = 1 

while cont <= 10: 
    print("ola, mundo!")
    cont += 1 # cont = cont + 1 
print("FIM")    

print(list(range(10)))
print(list(range(1,10,2)))

for cont in range(10):
    print("ola, munddo!")
print("FIM")     

soma = 0
for termo in range(1,11):
    soma += termo
print(soma)   

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

print(f"Soma: {n1 + n2}")
print(f"Produto: {n1 * n2}")

num = int(input("Digite um número inteiro positivo: "))

if num % 2 == 0:
    print(f"Resultado (Quadrado): {num ** 2}")
else:
    print(f"Resultado (Cubo): {num ** 3}")

num = int(input("Digite um número inteiro positivo: "))

if num % 2 == 0:
    print(f"Resultado (Quadrado): {num ** 2}")
else:
    print(f"Resultado (Cubo): {num ** 3}")

usuario = input("Usuário: ")
senha = input("Senha: ")

if (usuario == "procopio" and senha == "12345") or (usuario == "paiva" and senha == "54321"):
    print("Seja bem vindo!")
else:
    print("Usuário e senha não conferem")

senha_real = "123456"
tentativas = 3

while tentativas > 0:
    senha = input("Digite a senha: ")
    
    if senha == senha_real:
        print("Olá, <SEUNOME>. Seja bem-vindo ao nosso banco!")
        break
    else:
        tentativas -= 1
        if tentativas == 2:
            print("Senha incorreta! Você ainda tem 2 tentativas.")
        elif tentativas == 1:
            print("Senha incorreta! Você ainda tem 1 tentativa.")
        else:
            print("Sua senha foi bloqueada! Por favor, dirija-se a um de nossos caixas.")              
