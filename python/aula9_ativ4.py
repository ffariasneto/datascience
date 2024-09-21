class Veiculo:
    def __init__(self, marca):
        self.marca = marca
        self.velocidade = 0

class Carro(Veiculo):
    def acelerar(self):
        self.velocidade += 10
        print(f"{self.marca} acelerando,  velocidade atual: {self.velocidade} km/h")

    def frear(self):
        self.velocidade -= 10
        if self.velocidade < 0:
            self.velocidade = 0
        print(f"{self.marca} freando, velocidade atual:  {self.velocidade} km/h")


