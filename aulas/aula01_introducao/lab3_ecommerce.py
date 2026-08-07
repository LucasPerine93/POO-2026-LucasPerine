class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
    def aplicar_desconto(self, porcentagem):
        valorDesconto = (porcentagem / 100) * self.preco
        self.preco = self.preco - valorDesconto
        
        print(f"O desconto foi de {porcentagem}%")
        print(f"O valor do produto agora é: R${self.preco} \n")
        
    def exibir_dados(self):
        print(f"Nome do produto {self.nome}")
        print(f"Preco do produto: {self.preco}")
        
class Livro(Produto):
    def __init__(self, nome, preco, autor):
        super().__init__(nome, preco)
        self.autor = autor
        
    def exibir_dados(self):
        super().exibir_dados()
        print(f"Autor {self.autor} \n")
        
class Eletronico(Produto):
    def __init__(self, nome, preco, voltagem):
        super().__init__(nome, preco)
        self.voltagem = voltagem
        
    def exibir_dados(self):
        super().exibir_dados()
        print(f"Voltagem {self.voltagem} \n")
        
l1 = Livro("O Destino Chega", 49.99, "MARVEL")
e1 = Eletronico("Arduino UNO Q", 359.9, 3.3)

l1.exibir_dados()
l1.aplicar_desconto(30)
l1.exibir_dados()

e1.exibir_dados()
e1.aplicar_desconto(45)
e1.exibir_dados()

        
