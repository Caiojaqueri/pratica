n = int(input("Digite um número: "))
maior = n

for i in range(4):
    n2 = int(input("Digite outro número: "))
    if n2 > maior:
        maior = n2

print("O maior número digitado foi", maior)