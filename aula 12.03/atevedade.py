def somaecia(a, b):
    soma = a + b
    produto = a * b 
    return soma, produto

    print(f"soma: {soma}")
    print(f"produto: {produto}")


 def CalcularSalario(Hora, horasT):
    salarioT = Hora * horasT
    return salarioT

Hora = float(input("Digite o valor por hora: "))
horasT = float(input("Digite a quantidade de horas trabalhadas: "))

salario = CalcularSalario(Hora, horasT)

print("O salário total é: R$", salario)