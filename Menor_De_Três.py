n1 : int
n2 : int
n3 : int

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: " ))
n3 = int(input("Digite o terceiro número: " ))

if n1 < n2 and n1 < n3:
    print(f"Menor = {n1}")
elif n2 < n3 and n2 < n3:
    print(f"Menor = {n2}")
else:
    print(f"Menor = {n3}")



