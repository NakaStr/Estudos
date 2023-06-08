operador = input('Digite aqui o simbolo da operação que deseja, se for multiplicação *, soma +, divisão / e subitração -: \nSe deseja encerrar a calculadora digite sair: ')

while operador != 'sair':
    valor1 = int(input('Coloque aqui o primeiro numero: '))
    valor2 = int(input('Coloque aqui o segundo numero: '))
    if operador == "*":
        res = (valor1) * (valor2)
    elif operador == "+":
        res = (valor1) + (valor2)
    elif operador == "/":
        res = (valor1) / (valor2)
    elif operador == "-":
        res = (valor1) - (valor2)
    else:
        res = "Operação não suportada"

    print('O resultado da operação é: {}'.format(res))
    print('---------------------------------------')
    operador = input('Digite aqui o simbolo da operação que deseja, se for multiplicação *, soma +, divisão / e subitração -: \nSe deseja encerrar a calculadora digite sair: ')





