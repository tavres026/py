numeros = [80, 20, 30, 20, 40, 90, 50]

print("Lista:", numeros)

quantidade = len(numeros)
print("Quantidade de elementos:", quantidade)

vezes_20 = numeros.count(20)
print("O número 20 aparece:", vezes_20, "vezes")

posicao_30 = numeros.index(30)
print("Posição do número 30:", posicao_30)

existe_100 = 100 in numeros
print("O número 100 está na lista?", existe_100)




import random 

numeros = [91, 34, 67, 15, 82]

print("Lista original:", numeros)

numeros.sort()
print("Lista em ordem crescente:", numeros)

numeros.sort(reverse=True)
print("Lista em ordem decrescente:", numeros)

numeros3 = [6, 7, 8, 9, 10]

random.shuffle(numeros3)
print("Lista embaralhada:", numeros3)

numeross = [99, 79, 58, 3, 21, 9]

print("\nLista desafio:", numeross)

numeross.sort()
print("Ordem crescente:", numeross)

numeross.sort(reverse=True)
print("Ordem decrescente:", numeross)

random.shuffle(numeros4)
print("Lista embaralhada:", numeross)