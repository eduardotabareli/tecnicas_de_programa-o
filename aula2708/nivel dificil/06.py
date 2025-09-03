valor = float(input("Valor da compra: "))
tipo = input("Tipo de cliente (normal, premium, vip): ")

if tipo == "premium":
    desconto = 0.15
elif tipo == "vip":
    if valor > 200:
        desconto = 0.25
    else:
        desconto = 0.10
else:
    desconto = 0

valor_final = valor - (valor * desconto)
print("Valor a pagar:", valor_final)
