''' Faça um programa que pergunte quanto você ganha por hora
e o número de horas trabalhadas no mês. Calcule e mostre o total
do seu salário no referido mês, sabendo-se que são descontados 11%
para o Imposto de Renda, 8% para o INSS e 5% para sindicato,
faça um programa que nos dê:
1. Salário Bruto
2. Quanto pagou ao INSS.
3. Quanto pagou de IR.
4. Quanto pagou ao sindicato.
5. O Salário Líquido.

Calcule os descontos e o salário líquido, conforme a tabela abaixo:
'''

sal_hora = float(input("Digite o valor da hora trabalhada: "))
qtd_hora = float(input("Digite a quantidade de horas trabalhadas no mês: "))
sal_bruto = sal_hora * qtd_hora
inss = sal_bruto * 0.08
irpf = (sal_bruto - inss) * 0.11
sind = sal_bruto * 0.05
sal_liq = sal_bruto - inss - irpf - sind

print(f"Salário Bruto: R$ {sal_bruto:.2f}")
print(f"Valor Imposto de Renda: R$ {irpf:.2f}")
print(f"Valor INSS: R$ {inss:.2f}")
print(f"Valor Sindicato: R$ {sind:.2f}")
print(f"Salário Líquido: R$ {sal_liq:.2f}")