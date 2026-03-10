matricula1 = 2060001
nomw1 = "ana silva"
telefone1 = "9999-8888"

aluno = {
    "matricula": 2060001,
    "nome": "ana silva",
    "telefone": "9999-8888"
}

print(aluno)

contato = {
    "@camilaqueiroz" = "camila queiro.",
    "@brunamarequezine" = "bruna M.",
    "@sheromenezes" = "sheron M.",
    "@paolaoliveira" = "paola O."
}

print(contato)
print(type(contato))

print(contato["@camilaqueiroz"])

print(contato.get("@paolaoliveira"))
print(contato.get("@inexistente"))
print(contato.get("@paolaoliveira", "não encontrado"))

contato["@giovana"] = "giovana"
print("apos add ", contato)

contato["@paolaoliveira"] = "Paola Oliveira"
print("apos add: ", contato)

contato.update({
    "@brunamarquezine": "Bruna Marquezine"
    "@camilaqueiroz": "Camila Q."
})

print("apos atualizaçoes: ", contato)

removido = contato.pop("paolaoliveira")
print(f"removido: {removido}")
print("apos o pop: ", contato)

del contato["@camilaqueiroz"]
print("apos o del: ", contato)

copia = dict(contato)
contato.clear()
print("apos clear: ", contato)
print("copia: ", copia)

print("numero de contato: ", len(contato))

if "@joao" in contato;
    print(f"encontrado; {contato['@joao']}")


if "@inexistente" in contato:
    print("existe")

else:
    print("nao existe.")        