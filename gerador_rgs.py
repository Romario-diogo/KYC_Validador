import requests
import random

def gerar_nomes_com_genero(qtd_nomes):
    nomes_gerados = []
    usados = set()

    while len(nomes_gerados) < qtd_nomes:
        response = requests.get("https://randomuser.me/api/?nat=br&results=20")
        pessoas = response.json()['results']

        for pessoa in pessoas:
            genero = pessoa['gender']  # male ou female
            primeiro_nome = pessoa['name']['first']
            sobrenome_base = pessoa['name']['last']

            total_partes = random.randint(2, 4)

            sobrenomes = [sobrenome_base]
            while len(sobrenomes) < (total_partes - 1):
                sobrenome_extra = random.choice(pessoas)['name']['last']
                if sobrenome_extra not in sobrenomes:
                    sobrenomes.append(sobrenome_extra)

            nome_completo = f"{primeiro_nome} " + " ".join(sobrenomes)

            if nome_completo not in usados:
                usados.add(nome_completo)
                nomes_gerados.append((nome_completo, genero))

            if len(nomes_gerados) >= qtd_nomes:
                break

    return nomes_gerados


# def gerador_cpfs(numero):
#     cpf_gerados = []
#     cpf_usados = []

#     while numero 
    

numero = random.choices([0,1,2,3,4,5,6,7,8,9], k=11)

if numero[0] == 0:
    numero = random.choices([0,1,2,3,4,5,6,7,8,9], k=11)
else:
    numero = int("".join(map(str, numero)))
# while numero[0] == 0:
#     numero = random.choices([0,1,2,3,4,5,6,7,8,9], k=11)

#     print("Zero detectado ")
#     break
numero = f"{numero:011d}" 
cpf = f"{numero[:3]}.{numero[3:6]}.{numero[6:9]}-{numero[9:]}"
print(f"CPF: {cpf}")



# # Exemplo de uso
# for nome, genero in gerar_nomes_com_genero(1):
#     print(f"{nome} - {genero}")
