# Crie um programa que leia quantos dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere U$1,00 = R$3,27

dinheiro = float(input('Quanto dinheiro você tem na carteira? '))
dolares = dinheiro/3.27
print('Se você tem {}, então você poderá comprar {:.2F} dólares.'.format(dinheiro, dolares))
