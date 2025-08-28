numero = int(input("Digite um número: "))

if numero % 3 == 0 and numero % 5 == 0:
    print("Divisível por 3 e 5")
elif numero % 3 == 0:
    print("Divisível por 3")
elif numero % 5 == 0:
    print("Divisível por 5")
else:
    print("Não é divisível por 3 nem por 5")
