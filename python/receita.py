class Receita():
    def __init__(self, nome, tempo_preparo):
        self.nome = nome
        self.tempo_preparo = tempo_preparo
        self.ingredientes = []
        self.modo_preparo = ""
     
    def add_ingredientes(self, ingrediente, quantidade):
        self.ingredientes.append((ingrediente, quantidade))
    
    def preparo(self, modo_preparo):
        self.modo_preparo = modo_preparo

while True:
    print("Criar Receita!\n")
    name = input("Digite o nome da receita: ")
    while True:
        ingrediente = input("Digite o ingrediente: ")
        qtde = float(input("Digite a quantidade: "))
        continuar = input("Deseja adicionar mais ingredientes? S/N")
        if continuar == "N":
            break
        Receita.add_ingredientes(ingrediente, qtde)
    
            
    
             
    
        
     
     
     
     
     
     
     
     
     
     
     
     
     
     
        
    # def insert_ingredientes(self):
    #     item1 = input("Digite o primeiro ingrediente: ")
    #     item2 = input("Digite o segundo ingrediente: ")
    #     item3 = input("Digite o terceiro ingrediente: ")
    #     item4 = input("Digite o quarto ingrediente: ")
    #     self.ingredientes.append(item1, item2, item3, item4)
    #     return f"{item1}, {item2}, {item3}, {item4} são ingredientes da Receita de {self.nome}"


        