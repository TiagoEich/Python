# Faça um algoritmo que leia o salário de um funcionario e mostre seu novo salário, com 15% de aumento.

salario = float(input('Informe seu salário atual: R$'))
aumento = salario + (salario * 15 / 100)
print("Com um aumento de 15%, seu salário atual será de R${}.".format(aumento))