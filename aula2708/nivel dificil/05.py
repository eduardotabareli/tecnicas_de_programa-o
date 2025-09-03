numero_secreto = 7
acertou = False

while not acertou:
    chute = int(input("Adivinhe o número (1 a 10): "))
    if chute < numero_secreto:
        print("Muito baixo")
    elif chute > numero_secreto:
        print("Muito alto")
    else:
        print("Você acertou!")
        acertou = True
