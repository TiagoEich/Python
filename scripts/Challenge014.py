# Escreva um programa que converta uma temperatura digitada em °C e converta para °F

c = float(input('Informe a temperatura em em °C: '))
f = ((9 * c) / 5) + 32
print('Se a temperatura em graus é de {}°C, convertido para fahrenheit é de {}°F.'.format(c, f))

# Os parênteses não são necessários, pois a regra de precedência está correta
# A fórmula para converter de graus para fahrenheit é: 9 x graus celsius / 5 + 32
