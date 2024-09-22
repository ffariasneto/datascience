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
    
class Conta_corrente(Conta):
    def __init__(self, numero, titular, saldo, limite):
        super().__init__(numero, titular, saldo)
        self.limite = limite

    def sacar(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente, mesmo com o cheque especial!")
    
    def sacar_limite(self, valor):
        if self.saldo <= 0 and self.saldo + self.limite >= valor:
            self.saldo -= valor    
    
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
        tipo_conta = input("Esta é uma conta corrente? (s/n): ")

        if tipo_conta == "s":
            score = int(input("Informe o score do cliente (0-1000): "))
            limite = 0
            if score <= 300:
                limite = 250.0
                print(f"Limite de R$ {limite} concedido!")
            elif score <= 600:
                limite = 750.0
                print(f"Limite de R$ {limite} concedido!")
            elif score <= 1000:
                limite = 1500.0
                print(f"Limite de R$ {limite} concedido!")
            nova_conta = Conta_corrente(numero, titular, saldo, limite)
        else:
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
            if isinstance(conta, Conta_corrente):
                print(f"Conta: {conta.numero} - Titular: {conta.titular} - Saldo: R$ {conta.saldo} - Limite: R$ {conta.limite}")
            else:
                print(f"Conta: {conta.numero} - Titular: {conta.titular} - Saldo: R$ {conta.saldo}")                      

    elif main == "9":
        continuar = False
        print("Obrigado por usar o FTi Bank. Até logo!")
        break

    else:
        print("Opção inválida!")

 
