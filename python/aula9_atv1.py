class Forma:
    def  __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

class Retangulo(Forma):
    def area(self):
        resultado = self.altura * self.largura
        return resultado
    
    def perimetro(self):
        resultado = 2 * (self.altura + self.largura)
        return resultado
    
forma_1 = Retangulo(10, 30)
print(forma_1.area()) # 300


    

