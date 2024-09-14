class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return f'Nome: {self.nome}, Cargo: {self.cargo}, Salário: {self.salario}'

class Empresa:
    def __init__(self):
        self.funcionarios = []

    def adicionar_funcionario(self, nome, cargo, salario):
        novo_funcionario = Funcionario(nome, cargo, salario)
        self.funcionarios.append(novo_funcionario)

    def remover_funcionario(self, nome):
        self.funcionarios = [f for f in self.funcionarios if f.nome != nome]

    def listar_funcionarios(self):
        if not self.funcionarios:
            print("Nenhum funcionário cadastrado.")
        else:
            for funcionario in self.funcionarios:
                print(funcionario)

def menu():
    print("\n1. Adicionar Funcionário")
    print("2. Remover Funcionário")
    print("3. Listar Funcionários")
    print("4. Sair")
    return input("Escolha uma opção: ")

if __name__ == "__main__":
    empresa = Empresa()
    
    while True:
        opcao = menu()
        
        if opcao == '1':
            nome = input("Nome do funcionário: ")
            cargo = input("Cargo do funcionário: ")
            salario = float(input("Salário do funcionário: "))
            empresa.adicionar_funcionario(nome, cargo, salario)
            print(f"Funcionário {nome} adicionado.")
        
        elif opcao == '2':
            nome = input("Nome do funcionário a remover: ")
            empresa.remover_funcionario(nome)
            print(f"Funcionário {nome} removido.")
        
        elif opcao == '3':
            print("\nFuncionários:")
            empresa.listar_funcionarios()
        
        elif opcao == '4':
            print("Saindo...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")
