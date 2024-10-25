class ApartamentoPadrao():
    def __init__(self, num_quartos, ambientes_sala, num_banheiros, tem_area_servico, tem_varanda,
                 numero, valor):
        self.num_quartos = num_quartos
        self.ambientes_sala = ambientes_sala
        self.num_banheiros = num_banheiros
        self.tem_area_servico = tem_area_servico
        self.tem_varanda = tem_varanda
        self.numero = numero
        self.valor = valor
        self.disponibilidade = "Disponível"
    
    def acender_luz(self):
        print("Luzes acesas!")

    def abrir_cortina(self):
        print(f"As cortinas do apto {self.numero} estão abertas!")

class Studio(ApartamentoPadrao):
    def __init__(self, num_quartos, ambientes_sala, num_banheiros,
                 tem_area_servico, tem_varanda, numero, valor, cozinha_americana):
        self.cozinha_americana = cozinha_americana
        
        super().__init__(num_quartos, ambientes_sala, num_banheiros,
                         tem_area_servico, tem_varanda, numero, valor)

# # apto_605 = Apartamento(3, 3, 4, True, True, 605, 1500000)
# # print(apto_605.num_quartos)
# # print(f"O apartamento {apto_605.numero} tem {apto_605.num_quartos} quartos.")
# # apto_605.abrir_cortina()

# apto_101 = Apartamento(2, 2, 2, False, True, 101, 800000)
# print(f"O apartamento {apto_101.numero} tem {apto_101.num_quartos} quartos.")
# apto_101.abrir_cortina()

lista = []
while True:
    print("1 - Cadastrar Apartamento:")
    print("2 - Listar Apartamentos:")
    print("3 - Buscar valores por Apartamento:")
    print("4 - Sair:")
    op = input(": -> ")
    if op == 1:
        quartos = int(input("Digite o números de quartos: "))
        ambientes = int(input("Digite a qtde de ambientes da sala: "))
        banheiros = int(input("Digite o número de banheiros: "))
        area = input("Tem área de serviço? (S/N): ")
        varanda = int(input("Tem varanda? (S/N): "))
        numero = int(input("Digite o número do Apartamento: "))
        valor = int(input("Digite o valor do Apartamento: "))
        apto = ApartamentoPadrao(quartos, ambientes, banheiros, 
                           True if area == "S" else False,
                           True if varanda == "S" else False,
                           numero, valor)
        lista.append(apto)

    if op == 2:
        for apto in lista:
            print(f"O valor do apto {apto.numero} é R$ {apto.valor:.2f}.")

    if op == 3:
        apto_busca = int(input("Digite o número do apartamento: "))
        for apto in lista:
            if apto.numero == apto_busca:
                print(f"O valor do apto {apto.numero} é R$ {apto.valor:.2f}.")

    if op == 4:
        print("Saindo do programa...")
        break
