def cumprimento(texto):
    return (f"Olá, {texto}")

print(cumprimento("Lindsey de Vargas de Azevedo"))


import random

def media_sorteio():
    # atribui um valor inteiro entre 1 e 100 às variáveis n1, n2, n3 (sorteio)
    n1 = random.randint(0,100)
    n2 = random.randint(0,100)
    n3 = random.randint(0,100)

    media = sum([n1, n2, n3]) / 3 # três números aleatórios
    return media