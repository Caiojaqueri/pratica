lista = []

for i in range(5):
    n = int(input("Digite um número: "))
    lista.append(n)

    maior = lista[0]
    menor = lista[0]


    for i in lista:
        if i > maior:
            maior = i

    for x in lista:
        if x < menor: 
            menor = x

print("A lista de números digitados é:", lista) 
print("O maior número digitado foi", maior)
print("O menor número digitado foi", menor)