preço = int(input('Me diga o valor da peça a ser alterado: '))
desc = preço*5/100
newprice = preço-desc
print('O novo valor da peça é {} Com 5% de desconto'.format(newprice))
