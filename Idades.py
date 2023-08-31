nome1: str; nome2: str
idade: int


nome1 = str(input("Nome da primeira pessoa "))
idade1 = int(input("Idade: "))

nome2 = str(input("Nome da segunda pessoa: "))
idade2 = int(input("Idade: "))

media = (idade1 + idade2) / 2

print(f"A idade média de {nome1} e {nome2} é de {media}")
