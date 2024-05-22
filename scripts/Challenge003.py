# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela.

a = input('Digite algo: ')
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('É apenas  minúscula?', a.islower())
print('É apenas maiúsculo?',a.isupper())
print('É numérico? ', a.isnumeric())
print('É apenas espaços?', a.isspace())
print('É capitalizada?', a.istitle())
print('É decimal?', a.isdecimal())