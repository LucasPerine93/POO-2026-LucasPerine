class Veiculo:
    def __init__(self, marca, modelo, valor_diaria):
        self.marca = marca 
        self.modelo = modelo
        self.__valor_diaria = valor_diaria

    def get_valor_diaria(self):
        return self.__valor_diaria

    def calcular_aluguel(self, dias):
        return self.get_valor_diaria() * dias

class Carro(Veiculo):
    def __init__(self, marca, modelo, valor_diaria, portas):
        super().__init__(marca, modelo, valor_diaria)

        self.portas = portas

    def calcular_aluguel(self, dias):
        aluguel = super().calcular_aluguel(dias)

        return print(f"O valor do aluguel do carro é de R${aluguel + 50.0:.2f}")

class Moto(Veiculo):
    def __init__(self, marca, modelo, valor_diaria, cilindradas):
        super().__init__(marca, modelo, valor_diaria)

        self.cilindradas = cilindradas

    def calcular_aluguel(self, dias):
        aluguel = super().calcular_aluguel(dias)

        return  print(f"O valor do aluguel da moto é de R${aluguel - (aluguel * 0.10):.2f}")

frota = [
    Carro("Toyota", "Corolla", 150.0, 4),
    Moto("Honda", "CB 500", 100.0, 500)
]

print("--- RESUMO DOS ALUGUÉIS (3 DIAS) ---")

for veiculo in frota:
    veiculo.calcular_aluguel(3)
