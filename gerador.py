import csv
import random
import string


def gerar_id():
    caracteres = string.ascii_uppercase + string.digits
    codigo = ''.join(random.choices(caracteres, k=6))
    return f"AP-{codigo}"


def gerar_arquivo_csv(quantidade_linhas):
    with open("apostas.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        for _ in range(quantidade_linhas):
            numeros = random.sample(range(1, 61), 6)
            escritor.writerow([gerar_id()] + numeros)


if __name__ == "__main__":
    gerar_arquivo_csv(10)
    print("Arquivo apostas.csv gerado com sucesso!")