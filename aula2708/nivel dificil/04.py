senha = input("Digite uma senha: ")

if len(senha) >= 8:
    tem_maiuscula = False
    tem_numero = False
    for c in senha:
        if c >= "A" and c <= "Z":
            tem_maiuscula = True
        if c >= "0" and c <= "9":
            tem_numero = True
    if tem_maiuscula and tem_numero:
        print("Senha válida")
    else:
        print("Senha inválida")
else:
    print("Senha inválida")
