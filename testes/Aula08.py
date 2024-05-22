# import math
# num = int(input('Digite um número: '))
# raiz = math.sqrt(num)
# print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

# import math
# num = int(input('Digite um número: '))
# raiz = math.sqrt(num)
# print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))

# from math import sqrt
# num = int(input('Digite um número: '))
# raiz = sqrt(num)
# print('A raiz de {} é igual a {}'.format(num, raiz))

#desse jeito, a raiz quadrada ja vai vir embutida na biblioteca de matemática.

from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz quadrada de {} é {}'.format(num, floor(raiz)))
