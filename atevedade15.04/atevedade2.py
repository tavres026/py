produto1 = float(input("digite o valor do primeiro produto: "))
produto2 = float( input("digite o valor do segundo produto:"))

def calcular_total(produto1, produto2):
    return produto1 + produto2

print(f"o total a pagar e: {calcular_total(produto1, produto2)}")