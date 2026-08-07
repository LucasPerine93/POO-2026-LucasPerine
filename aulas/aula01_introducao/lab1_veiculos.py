class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
class Carro(Veiculo):
    def __init__(self, marca, modelo, qtd_portas):
        super().__init__(marca, modelo)
        self.qtd_portas = qtd_portas
        
c1 = Carro("Bugatti", "Chiron", 2)

print(f"Marca: {c1.marca} | Modelo: {c1.modelo} | N° portas {c1.qtd_portas}")