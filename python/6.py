class Funcionario:
    def __init__(self, nome, funcao, salario):
        self.nome = nome
        self.funcao = funcao
        self.salario = salario

class Quarto:
    def __init__(self, numero, tipo, preco):
        self.numero = numero
        self.tipo = tipo
        self.preco = preco
        self.reservado = False

class Reserva:
    def __init__(self, nome_cliente, quarto, dias):
        self.nome_cliente = nome_cliente
        self.quarto = quarto
        self.dias = dias

    def calcular_conta(self):
        return self.dias * self.quarto.preco

class Hotel:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []
        self.quartos = []
        self.reservas = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def adicionar_quarto(self, quarto):
        self.quartos.append(quarto)

    def fazer_reserva(self, nome_cliente, tipo_quarto, dias):
        for quarto in self.quartos:
            if quarto.tipo == tipo_quarto and not quarto.reservado:
                quarto.reservado = True
                reserva = Reserva(nome_cliente, quarto, dias)
                self.reservas.append(reserva)
                return reserva
        return None

    def calcular_conta_final(self, nome_cliente):
        total = 0
        for reserva in self.reservas:
            if reserva.nome_cliente == nome_cliente:
                total += reserva.calcular_conta()
        return total

# Exemplo de uso
hotel = Hotel("Hotel Exemplo")

# Adicionando funcionários
hotel.adicionar_funcionario(Funcionario("João", "Recepcionista", 2000))
hotel.adicionar_funcionario(Funcionario("Maria", "Camareira", 1500))

# Adicionando quartos
hotel.adicionar_quarto(Quarto(101, "Simples", 100))
hotel.adicionar_quarto(Quarto(102, "Luxo", 200))

# Fazendo uma reserva
reserva = hotel.fazer_reserva("Carlos", "Simples", 3)
if reserva:
    print(f"Reserva feita para {reserva.nome_cliente} no quarto {reserva.quarto.numero} por {reserva.dias} dias.")

# Calculando a conta final
conta_final = hotel.calcular_conta_final("Carlos")
print(f"Conta final para Carlos: R${conta_final}")