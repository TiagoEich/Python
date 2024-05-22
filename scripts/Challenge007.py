# Escreva um programa que leia um programa que leia um valor em metros e o exiba convertido em km, hm, dam, dm, cm, mm

m = int(input('Informe uma distância em metros:'))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('{} quilômetros\n{} hectômetros\n{} decâmetros\n{} decímetros\n{} centímetros\n{} milímetros'.format(km, hm, dam, dm, cm, mm))
