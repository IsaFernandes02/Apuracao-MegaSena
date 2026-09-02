import csv
import random
import string
import sys


def gerar_id():
    caracteres = string.ascii_uppercase + string.digits
    codigo = ''.join(random.choices(caracteres, k=6))
    return f"AP-{codigo}"

if len(sys.argv) > 1:
    num_linhas = int(sys.argv[1])
else:
    num_linhas = 10

with open("apostas.csv", "w", newline="") as arquivo:
    escritor = csv.writer(arquivo)

    for _ in range(num_linhas):
        quantidade_numeros = random.randint(6, 15)
        numeros = random.sample(range(1, 61), quantidade_numeros)

        if 6 <= len(numeros) <= 15:
            escritor.writerow([gerar_id()] + numeros)

print(f"Arquivo apostas.csv gerado com sucesso com {num_linhas} apostas!")