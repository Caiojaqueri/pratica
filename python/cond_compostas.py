salario = float(input("Digite seu salário: "))

if salario <= 3000:
    print("Programador junior")
elif salario > 3000 and salario <= 6000:
    print("Programador pleno")
elif salario > 6000 and salario <=15000:
    print("Programador senior")
else: 
    print("Programador master")
