reais = float(input("Digite o valor em reais: "))
moeda = input("Digite a moeda de destino (dólar ou euro): ")

if moeda == "dólar":
    print("Valor em dólar:", reais / 5)
elif moeda == "euro":
    print("Valor em euro:", reais / 5.5)
else:
    print("Moeda inválida")
