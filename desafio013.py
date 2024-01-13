"""Faça um algorítmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento"""

salario = float(input('Digite o valor do seu salário: '));

print('O valor do salário com acréscimo de 15% é R${:.2f}'.format(salario + salario * 0.15))