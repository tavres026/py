paciente = {}

paciente["nome"] = input("qual o seu nome: ")
paciente["idade"] = int(input("quantos anos voce tem: "))
paciente["peso"] = float(input("digite seu peso; "))
paciente["altura"] = float(input("digite sua altura: "))

imc = paciente["peso"] / (paciente["altura"] ** 2)

paciente["imc"] = imc

print("\n dados")
print("nome:", paciente["nome"])
print("idade: ", paciente["idade"])
print("peso: ", paciente["peso"])
print("altura: ", paciente["altura"])
print("IMC: ", round(paciente["altura"], 2))