''' Crie um programa que solicite ao usuário que digite números inteiros.
O programa deve continuar solicitando número até que a soma dos números pares digitados seja 
maior que 50. Ao atingir ou ultrapassar esse limite, o programa deve exibir a soma
total e encerrar.
Dica:
1. Use um loop while para continuar solicitando números até que a condição seja atendida.
2. Mantenha uma variável para rastrear a soma dos números pares.
3. Utilize a instrução break para sair do loop quando a condição for atendida.
4. Exiba a soma total ao final.
'''

pares = 0
while True:
    num = int(input("Digite um número aleatório: "))
    if num % 2 == 0:
        pares += num
    print(f"Soma atual dos número pares: {pares}")
    if pares >= 50:
        break
print(pares)