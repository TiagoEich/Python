# Ler o preço do produto e informar o preço com desconto em pagamento a vista e com aumento para parcelado. A vista 10% de desconto e parcelado 8% de aumento.

preco = float(input('Informe o valor do seu produto: R$'))
aumento = preco + (preco * 8 / 100)
desconto = preco - (preco * 10 / 100)
print('Seu produto a vista será de R${:.2f} e parcelado de R${:.2f}.'.format(desconto, aumento))


