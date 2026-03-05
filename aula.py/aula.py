nomes = ["ana", "bruno", "carlos", "diana"]
print("nome: ", nomes)

nomes.remove("bruno")
print("lista atualizada: ", nomes)

removido = nomes.pop(1)
print(f"removido: {removido}")
print("apos pop(): ", nomes)

del nomes[0]
print("após del nome[0]")

nomes.clear()
print("lista atualizada: ", nomes)