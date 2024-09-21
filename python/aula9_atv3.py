# class Calculadora:
#     def somar(self, a, b):
#         if isinstance(a, int) and isinstance(b, int):
#             return a + b
#         elif isinstance(a, str) and isinstance(b, str):
#             return a + b
#         else:
#             return "Erro: tipos de dados diferentes"
        
# calc = Calculadora()

# sum_int = calc.somar(10,  20)
# print(sum_int) # 30

# sum_str = calc.somar("Francisco ", "Farias")
# print(sum_str) # Francisco Farias

class Calculadora:
    def somar(self, a, b):
        if type(a is int) and type(b is int):
            return a + b
        elif type(a is str) and type(b is str):
            return a + b
        else:
            return "Erro: tipos de dados diferentes"
        
calc = Calculadora()

sum_int = calc.somar(10,  20)
print(sum_int) # 30

sum_str = calc.somar("Francisco ", "Farias")
print(sum_str) # Francisco Farias


        