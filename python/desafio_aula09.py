class Conta:
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.resumo = []

    def registrar_movimentacao(self, tipo, valor):
        self.resumo.append(f"{tipo}: {valor:.2f}")
            
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.registrar_movimentacao("Saque", valor)
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente!")
    
    def depositar(self, valor):
        self.saldo += valor
        self.registrar_movimentacao("Depósito", valor)
        print("Deposito realizado com sucesso!")
    
    def saldo_atual(self):
        return self.saldo
    
    def mostrar_resumo_movimentacoes(self):
        if self.resumo:
            print(f"Resumo das movimentações da conta {self.numero}.")
            for movimento in self.resumo:
                print(movimento)
        else:
            print("Nenhuma movimentação encontrada!")
    
class Conta_corrente(Conta):
    def __init__(self, numero, titular, saldo, limite):
        super().__init__(numero, titular, saldo)
        self.limite = limite

    def sacar(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.registrar_movimentacao("Saque com cheque especial", valor)
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente, mesmo com o cheque especial!")
    
    def sacar_limite(self, valor):
        if self.saldo <= 0 and self.saldo + self.limite >= valor:
            self.saldo -= valor

class Conta_poupanca(Conta):
    def __init__(self, numero, titular, saldo, juros):
        super().__init__(numero, titular, saldo)
        self.juros = juros

    def depositar(self, valor):
        self.saldo += valor
        self.registrar_movimentacao("Depósito", valor)
        self.aplicar_juros()
    
    def aplicar_juros(self):
        rendimento = self.saldo * self.juros
        self.saldo += rendimento
        self.registrar_movimentacao("Aplicação dos juros", rendimento)
        print(f"Juros aplicados! Saldo atual: R$ {self.saldo:.2f}")


ftibank = []
continuar = True

while continuar == True:
    print("Bem-vindo(a) ao FTi Bank")
    print("1 - Criar conta")
    print("2 - Sacar dinheiro")
    print("3 - Depositar dinheiro")
    print("4 - Ver saldo")
    print("5 - Resumo das Movimentações")
    print("8 - Listar Contas")
    print("9 - Sair")

    main = input(": -> ")

    if main == "1":
        numero = input("Digite o número da conta: ")
        titular = input("Digite o nome do titular: ")
        saldo = float(input("Digite o valor inicial da conta: "))
        print("Qual tipo de conta para cadastro?")
        print("1.1 - Conta")
        print("1.2 - Conta Corrente")
        print("1.3 - Conta Poupança")
        tipo_conta = input(": ->  ")

        if tipo_conta == "1.2":
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
                print("Conta Corrente cadastrada!")
            nova_conta = Conta_corrente(numero, titular, saldo, limite)
        elif tipo_conta == "1.3":
            juros = float(input("Digite a taxa de juros (em decimal, ex: 0.05 para 5%): "))
            nova_conta = Conta_poupanca(numero, titular, saldo, juros)
            print("Conta Poupança cadastrada!")
        else:
            nova_conta = Conta(numero, titular, saldo)
            print("Conta cadastrada!")

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
    
    elif main == "5":
        numero = input("Digite o número da conta: ")
        conta_encontrada = False

        for conta in ftibank:
            if conta.numero == numero:
                conta.mostrar_resumo_movimentacoes()
                conta_encontrada = True
                break
        
        if not conta_encontrada:
            print("Conta não encontrada!")

    elif main == "8":
        for conta in ftibank:
            if isinstance(conta, Conta_corrente):
                print(f"Conta: {conta.numero} - Titular: {conta.titular} - Saldo: R$ {conta.saldo} - Limite: R$ {conta.limite}")
            elif isinstance(conta, Conta_poupanca):
                print(f"Conta: {conta.numero} - Titular: {conta.titular} - Saldo: R$ {conta.saldo}")
            else:
                print(f"Conta: {conta.numero} - Titular: {conta.titular} - Saldo: R$ {conta.saldo}")                      

    elif main == "9":
        continuar = False
        print("Obrigado por usar o FTi Bank. Até logo!")
        break

    else:
        print("Opção inválida!")

 

