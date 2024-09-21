class Veiculo:
    def __init__(self, cor, modelo):
        self.cor = cor
        self.modelo = modelo

class Carro(Veiculo):
    def setCor(self, nova_cor):
        self.cor = nova_cor

fiesta = Carro("Azul", "Fiesta")
fiesta.setCor("Vermelho")
print(fiesta.cor)
