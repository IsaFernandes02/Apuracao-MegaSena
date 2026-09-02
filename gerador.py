import csv
import random
import string


def gerar_id():
    caracteres = string.ascii_uppercase + string.digits
    codigo = ''.join(random.choices(caracteres, k=6))
    return f"AP-{codigo}"


with open("apostas.csv", "w", newline="") as arquivo:
    escritor = csv.writer(arquivo)

    for _ in range(10):
        quantidade_numeros = random.randint(6, 15)
        numeros = random.sample(range(1, 61), quantidade_numeros)

        if 6 <= len(numeros) <= 15:
            escritor.writerow([gerar_id()] + numeros)

print("Arquivo apostas.csv gerado com sucesso!")