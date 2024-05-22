# Faça um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço = float(input('Informe o valor de seu produto: '))
desconto = preço - (preço * 5 / 100)
print('O valor final com o desconto de 5% será de R${}'.format(desconto))
