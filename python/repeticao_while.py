notas = []
contador = 1

while contador <= 5: #enquanto o contador foi menor ou igual a 1
    codigo_aluno = input("RM: ")
    nome = float(input("NOTA: "))
    resultado = [codigo_aluno, nome]
    notas.append(resultado)

    contador += 1

print("quantidade de notas:", len(notas))