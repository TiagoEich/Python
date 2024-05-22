# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

"""import math
angulo = float(input('Informe um ângulo: '))
seno = math.sin(math.radians(angulo))
print("O Ângulo {} tem o SENO de {:.2f}.".format(angulo,seno))
cosseno = math.cos(math.radians(angulo))
print("O Ângulo {} tem o COSSENO de {:.2f}.".format(angulo,cosseno))
tangente = math.tan(math.radians(angulo))
print("O ângulo {} tem a TANGENTE de {:.2f}.".format(angulo,tangente)) """


from math import sin, cos, tan, radians
angulo = float(input("Digite o valor do ângulo: "))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print("O ângulo de {} tem o seno de {:.2f}\nO ângulo de {} tem o cosseno de {:.2f}\nO ângulo de {} tem a tangente de "
      "{:.2f}".format(angulo, seno, angulo, cosseno, angulo, tangente))
