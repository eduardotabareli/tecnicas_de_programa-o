senha_correta = "python123"
tentativas = 0

while tentativas < 3:
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        print("Login bem-sucedido")
        break
    else:
        tentativas += 1
        print("Senha incorreta")
else:
    print("Conta bloqueada")
