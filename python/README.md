# Desafio Conta Bancária
## Sistema de gerenciamento de contas bancárias em Python
Crie um sistema de gerenciamento de contas bancárias em Python usando herança e polimorfismo. O sistema deve incluir as seguintes classes:
### Classe Conta
- A classe base "Conta" deve ter atributos para o número da conta, o titular da conta e o saldo.
- Ela deve incluir métodos para depósitos, saques e exibição do saldo atual.
### Classe Conta Corrente
- A classe "Conta Corrente" herda de "Conta" e inclui atributos específicos, como taxa de manutenção e limite de cheque especial.
- Deve sobrescrever o método de saque para considerar o limite de cheque especial, se necessário.
### Classe Conta Poupança
- A classe "Conta Poupança" também herda de "Conta" e inclui atributos específicos, como taxa de juros.
- Ela deve ter um método para calcular e adicionar juros ao saldo.
- Crie um método chamado resumo que pode ser chamado em qualquer objeto de conta (Conta Corrente ou Conta Poupança). Esse método resumo irá exibir um resumo das informações da conta, incluindo o tipo de conta (corrente ou poupança), o número da conta, o titular da conta e o saldo atual.
### Teste de Funcionalidade
Crie um programa principal que demonstre o uso dessas classes. Crie instâncias de contas correntes e poupanças, realize depósitos, saques, adicione juros e chame o método resumo para cada conta.
# Classe Conta
```
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
```
- Definida classe "Conta", função construtora, delimitando número, titular e saldo inicial da conta.
- Definida função sacar valor, caso o saldo seja maior ou igual ao valor informado para saque, o programa vai efetuar o saque, caso contrário, informará que não há saldo suficiente.
- Definida função depositar valor, quando o usuário selecionar a opção de depósito no menu, o sistema vai acrescentar ao saldo, o valor informado pelo usuário.
- Definida função saldo atual, quando o usuário escolher a opção de verificar saldo, o programa vai mostrar o saldo atual da conta.
# Classe Conta Corrente
```
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
```
- Definida classe "Conta Corrente", função construtora, delimitando número, titular, saldo e limite, trouxe o método super() para recuperar uma função da Classe "Conta".
- Definida função sacar valor, caso o saldo + limite seja maior ou igual ao valor solicitado pelo usuário, o programa irá deduzir do saldo e realizará o saque, caso contrário, não efetuará o saque e informará que o usuário não tem saldo, nem limite.
- Definida função sacar_limite, caso o saldo seja menor que zero e o saldo + limite seja maior que o valor informado pelo usuário, o programa efetuará o saque.
