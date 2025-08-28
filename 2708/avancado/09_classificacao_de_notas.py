notas = [9, 6, 4, 7, 5]

for nota in notas:
    if nota >= 7:
        print("Nota", nota, ": Aprovado")
    elif nota >= 5:
        print("Nota", nota, ": Recuperação")
    else:
        print("Nota", nota, ": Reprovado")
