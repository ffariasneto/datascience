class Calculadora:
    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        if b == 0:
            return "Divisão por zero dá zero"
        return a / b

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
calc = Calculadora()
print("Soma: ", calc.soma(a, b))
print("Subtração: ", calc.subtracao(a, b))
print("Multiplicação: ", calc.multiplicacao(a, b))
print("Divisão: ", calc.divisao(a, b))
