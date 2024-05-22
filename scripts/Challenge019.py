# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice
aluno = input("Primeiro aluno: ")
aluno2 = input("Segundo aluno: ")
aluno3 = input("Terceiro aluno: ")
aluno4 = input("Quarto aluno: ")
alunos = [aluno, aluno2, aluno3, aluno4]
escolhido = choice(alunos)
print("O aluno escolhido é {}!".format(escolhido))