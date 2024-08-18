"""
Simples código para calcular o fatorial de um número
"""
number = int(input('Qual o número deseja calcular o fatorial: '))
fatorial = 1

for contador in range(1, number+1):
    fatorial *= contador

print(f'O fatorial de {number} é {fatorial}')
