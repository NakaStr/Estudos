import random 
a1 = input(('Coloque aqui o nome do primeiro aluno: '))
a2 = input(('Coloque aqui o nome do segundo aluno: '))
a3 = input(('Coloque aqui o nome do terceiro aluno: '))
a4 = input(('Coloque aqui o nome do quarto aluno: '))
sor = a1,a2,a3,a4
print('Os alunos escolhidos para o sorteio são:\n{} \n{} \n{} \n{} \nO aluno sorteado foi: {} !!!!!!!!!!'.format(a1, a2, a3, a4, random.choice(sor)))
