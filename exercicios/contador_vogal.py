palavra = input("Digite uma palavra: ")
contador = 0

for i in range(len(palavra)):
    if palavra[i].lower() in "aeiou":
        contador += 1

print("A palavra", palavra, "tem", contador, "vogais.")