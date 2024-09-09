# 1. Faça um programa que peça dois números e imprima a soma.
num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
soma = num1 + num2
print(f"O resultado da soma é: {soma}.")

# 2. Faça um programa que peça as 4 notas bimestrais e mostre a média.
nota1 = float(input("Digite a nota do primeiro bimestre: "))
nota2 = float(input("Digite a nota do segundo bimestre: "))
nota3 = float(input("Digite a nota do terceiro bimestre: "))
nota4 = float(input("Digite a nota do quarto bimestre: "))
soma = nota1 + nota2 + nota3 + nota4
media = soma / 4
print(f"A média do aluno no ano, foi: {media}.")

# 3. Faça um programa que converta metros para centímetros.
print("Conversor de Metros para Centímetros")
metro = float(input("Digite o valor em metros: "))
conv = metro * 100
print(f"{metro} m, equivale a {conv} cm.")

''' 4. Faça um programa que calcule a área de um quadrado, em
seguida mostre o dobro desta área para o usuário.
'''
lado1 = float(input("Digite o valor do primeiro lado do quadrado: "))
lado2 = float(input("Digite o valor do segundo lado do quadrado: "))
area = lado1 * lado2
dobro = area * 2
print(f"A área do quadrado é: {area} e o dobro desta área é: {dobro}")

''' 5. Faça um programa que pergunte quanto você ganha por hora
e o número de horas trabalhadas no mês. Calcule e mostre o total
do seu salário no referido mês.
'''
sal_h = float(input("Qua o valor da sua hora trabalhada? "))
qtd_h = float(input("Quantas horas você trabalha no mês? "))
salario = sal_h * qtd_h
print(f"O valor do seu salário no mês, é de: R$ {salario}.")