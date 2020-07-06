# -*- coding: utf-8 -*-

"""

Calculadora
Autor Valdir Mariano
Função: Fazer contas - Soma, Divisão, Multiplicação, Subtração.

"""

print(  

	"- - - - - - CALCULADORA v2.0 - - - - - -")

sair = False  

while sair == False:

	valor1 = input("Digite o Primeiro Número: ")
	valor1 = float(valor1)
	operador = input("Digite o Operador (+) = soma (-) = subtração (/) = divisão (*) multiplicação (**) exponenciação: ")
	valor2 = input("Digite o Segundo Número: ")
	valor2 = float(valor2)

	# + soma
	if operador == "+":
		operacao = valor1 + valor2


	# - subtração
	if operador == "-":
		operacao = valor1 - valor2

	# / divisão
	if operador == "/":
		operacao = valor1 / valor2

	# * multiplicação
	if operador == "*":
		operacao = valor1 * valor2

	# ** exponenciação 
	if operador == "**":
		operacao = valor1 ** valor2

	print("Resultado: ")
	print(operacao)

	teste = input("Deseja Sair? (s/n): ")
	if teste == "s":
		sair = True