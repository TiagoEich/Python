# Faça um programa que leia a largura e a altura de uma parede em metros. calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²

largura = float(input('Informe o valor da largura: '))
altura = float(input('Informe o valor da altura: '))
area = largura * altura
print('Sua parede tem a dimensão de {}x{} e sua área é de {:.2f}m²'.format(largura, altura, area))
tinta = area / 2
print('Você precisará de {:.2f} litros de tinta para pintar sua parede.'.format(tinta))
