class Conta:
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente!")
    
    def depositar(self, valor):
        self.saldo += valor
        print("Deposito realizado com sucesso!")
    
    def saldo_atual(self):
        return self.saldo
    
ftibank = []
continuar = True

while continuar == True:
    print("Bem-vindo(a) ao FTi Bank")
    print("1 - Criar conta")
    print("2 - Sacar dinheiro")
    print("3 - Depositar dinheiro")
    print("4 - Ver saldo")
    print("8 - Listar Contas")
    print("9 - Sair")

    main = input(": -> ")

    if main == "1":
        numero = input("Digite o número da conta: ")
        titular = input("Digite o nome do titular: ")
        saldo = float(input("Digite o valor inicial da conta: "))
        nova_conta = Conta(numero, titular, saldo)
        ftibank.append(nova_conta)

    elif main == "2":
        numero = input("Digite o número da conta: ")
        vlr_saque = float(input("Qual valor deseja sacar? "))
        conta_encontrada = False

        for conta in ftibank:
            if conta.numero == numero:
                conta.sacar(vlr_saque)
                conta_encontrada = True
                break

        if not conta_encontrada:
            print("Conta não encontrada!")

    elif main == "3":
        numero = input("Digite o número da conta: ")
        vlr_deposito = float(input("Qual valor deseja depositar? "))
        conta_encontrada = False

        for conta in ftibank:
            if conta.numero == numero:
                conta.depositar(vlr_deposito)
                conta_encontrada = True
                break
        
        if not conta_encontrada:
            print("Conta não encontrada!")


    elif main == "4":
        numero = input("Digite o número da conta: ")
        conta_encontrada = False

        for conta in ftibank:
            if conta.numero == numero:
                print(f"Saldo atual: {conta.saldo_atual()}")
                conta_encontrada = True
                break

        if not conta_encontrada:
            print("Conta não encontrada!")

    elif main == "8":
        for conta in ftibank:
            print(f"Conta: {conta.numero} - Titular: {conta.titular} - Saldo: R$ {conta.saldo}")

    elif main == "9":
        continuar == False
        print("Obrigado por usar o FTi Bank. Até logo!")
        break

    else:
        print("Opção inválida!")

 

