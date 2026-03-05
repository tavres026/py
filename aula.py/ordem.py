import random

numeros = [45, 12, 78, 23, 56]
print("lista original: ", numeros)

numeros.sort()
print("após sort(): ", numeros)

numeros.sort(reverse=True)
print("após sort(): ", numeros)

random.shuffle(numeros)
print("lista embaralhada: ", numeros)