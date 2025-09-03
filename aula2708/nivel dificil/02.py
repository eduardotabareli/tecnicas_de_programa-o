a = int(input("Lado 1: "))
b = int(input("Lado 2: "))
c = int(input("Lado 3: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b and b == c:
        print("Triângulo equilátero")
    elif a == b or a == c or b == c:
        print("Triângulo isósceles")
    else:
        print("Triângulo escaleno")
else:
    print("Não é um triângulo válido")
