'''Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua posição inteira.
ex: Digite um número: 6.127
O número 6.127 tem a parte inteira 6'''


'''from math import trunc
real = float(input('Digite um número real: '))
inteiro = trunc(real)
print('O número {} tem a parte inteira {}'.format(real, inteiro))'''

from math import trunc
real = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}'.format(real, trunc(real)))

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, int(num)))