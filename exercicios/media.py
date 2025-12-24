nota1 = float(input("Nota da Primeira prova: "))
nota2 = float(input("Nota da Segunda prova: "))
nota3 = float(input("Nota da Terceira prova: "))

media = (nota1 + nota2 + nota3) / 3
print("A média das notas é:", media)

if media >= 6:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")
    