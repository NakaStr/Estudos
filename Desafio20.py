import random
a1 = input('Nome do primeiro aluno: ')
a2 = input('Nome do segundo aluno: ')
a3 = input('Nome do terceiro aluno: ')
a4 = input('nome do quardo aluno: ')
list = [a1, a2, a3, a4]
sor = random.sample(list, k=4)
print('A ordem para a apresentação dos trabalhos é: {}'.format(random.sample(sor, k=4)))