import math

base = float(input("DIgite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))

area = base * altura
perimetro = 2 * (base + altura)
diagonal = math.sqrt(math.pow(base, 2) + math.pow(altura, 2))


print(f"Area: {area}")
print(f"Perimetro: {perimetro}")
print(f"diagonal: {diagonal}")


