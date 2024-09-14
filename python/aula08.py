# class Cachorro:
#     def __init__(self, nome, idade, raca):
#         self.nome = nome
#         self.idade = idade
#         self.raca = raca
    
#     def __str__(self):
#         return f"Cachorro(nome={self.nome}, raca={self.raca},  idade={self.idade})"



# class Pessoa:
#     def __init__(self, nome, idade, peso, genero):
#         self.nome = nome
#         self.idade = idade
#         self.peso = peso
#         self.genero = genero
    
#     def __str__(self):
#         return f"Pessoa(nome={self.nome}, idade={self.idade}, peso={self.peso}, genero={self.genero})"


class Funcionarios:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

class Empresa:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.funcionarios = []
    
    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
    
    def remover_funcionario(self,  funcionario):
        self.funcionarios.remove(funcionario)
    
    def listar_funcionario(self):
        for funcionario in self.funcionarios:
            print(f"Nome: {funcionario.nome}, Cargo: {funcionario.cargo}, Salario: {funcionario.salario:.2f}")

continuar = True
while continuar == True:
    cad_nome = input("Digite o nome do funcionário: ")
    cad_cargo = input("Digite o cargo do funcionário: ")
    cad_salario = float(input("Digite o salario do funcionário: "))
    funcionario = Empresa(cad_nome, cad_cargo, cad_salario)
    funcionarios.append(funcionario)
    cont = bool(input("Digite True, caso deseja continuar ou False para encerrar: "))
    if cont == False:
        continuar = False
        print("Lista de funcionários:")
        for funcionario in funcionarios:
            funcionario.listar_funcionario()
            print("\n")  # Adicione uma quebra de linha para melhorar a leg
            break

    
 
    


