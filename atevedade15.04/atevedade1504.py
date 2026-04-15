nota1 = float(input ("digite a primeira nota:"))
nota2 = float(input ("digite a segunda nota:"))
nota3 = float(input ("digite a terceira nota:"))

def media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

print(f"a media das notas e: {media(nota1, nota2, nota3):.2f}")    