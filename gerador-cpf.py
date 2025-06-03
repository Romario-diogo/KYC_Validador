# Criar um gerador de CPF
# tecnologias usadas 
import random

usado = set()

# Gerador de numero com 11 numeros
while True:
    numero= random.choices(range(10),k=11)

# CPF com 0 no inicio descartar 
    if numero[0] == 0:
        continue

    numero_str = ''.join(map(str, numero))

    if numero_str not in usado:
        usado.add(numero_str)
        print("CPF Gerado ", numero_str)
        # Formata no pafrão 000.000.000-00
        cpf = f"{numero_str[:3]}.{numero_str[3:6]}.{numero_str[6:9]}-{numero_str[9:]}"

        print(f"CPFs: {cpf}")

        break

# Criar um padrão de CPF.
# Comparar com numeros ja criados 
# Descartar Combinações do mesmo CPF

