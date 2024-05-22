"""Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado"""

km = float(input('Km percorridos: '))
dia = int(input('Dias alugados: '))
kms = km * 0.15
dias = dia * 60
total = kms + dias
print('Se você alugou por {} dias e percorreu {}km, o valor final do aluguel é de R${:.2f}'.format(dia, km, total))