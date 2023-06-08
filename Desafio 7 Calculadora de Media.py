nome = input('Nome do Aluno: ')
nota1 = int(input('Insira a nota da Avaliação Pratica: '))
nota2 = int(input('Insira a nota de Comportamento: '))
nota3 = int(input('Insira a nota da Avaliação Teorica: '))
media = (nota1 + nota2  + nota3) / 3
print('A media do aluno {} é: {}'.format(nome, media))