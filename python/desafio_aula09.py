class Conta:
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
    
    def sacar(self):
        if self.saldo >= 100:
            self.saldo -= 100
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente!")
    
    def depositar(self):
        self.saldo += 100
        print("Deposito realizado com sucesso!")
    
    def saldo_atual(self):
        return self.saldo
    

contas = {}

print("Bem-vindo(a) ao FTi Bank")
print("1 - Criar conta")
print("2 - Sacar dinheiro")
print("3 - Depositar dinheiro")
print("4 - Ver saldo")
main = input(": -> ")
if main == "1":
    numero = input("Digite o número da conta: ")
    contas["Conta"] = numero
    titular = input("Digite o nome do titular: ")
    contas["Titular"] = titular
    saldo = float(input("Digite o valor inicial da conta: "))
    contas["Saldo"] = saldo
elif main == "2":
    numero = input("Digite o número da conta: ")
    titular = input("Digite o nome do titular: ")
    conta = Conta(numero, titular, input("Qual valor deseja sacar? "))
elif main == "3":
    numero = input("Digite o número da conta: ")
    titular = input("Digite o nome do titular: ")
    conta = Conta(numero, titular, input("Qual valor deseja depositar? "))
elif main == "4":
    numero = input("Digite o número da conta: ")
    titular = input("Digite o nome do titular: ")
    conta = Conta(numero, titular, input("Qual valor deseja verificar? "))
else:
    print("Opção inválida!")

print(contas)




# cont = Conta(1234, "Francisco",  1000)
# print(cont.saldo_atual()) # 1000
# cont.sacar()
# print(cont.saldo_atual()) # 900

