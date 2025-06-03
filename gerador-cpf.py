# Criar um gerador de CPF
# tecnologias usadas 
import random
# Gerador de numero com 11 numeros
numero = random.choices([0,1,2,3,4,5,6,7,8,9], k=11)

# CPF com 0 no inicio descartar 
if numero[0] == 0:
    numero = random.choices([0,1,2,3,4,5,6,7,8,9], k=11)
else:
    print(numero)
# Criar um padrão de CPF.
# Comparar com numeros ja criados 
# Descartar Combinações do mesmo CPF

