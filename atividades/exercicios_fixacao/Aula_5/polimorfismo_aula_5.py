from abc import ABC, abstractmethod

class Veiculo:
    def __init__(self, modelo):
        self.modelo = modelo

    @abstractmethod
    def acelerar(self):
        pass

class Carro(Veiculo):
    def __init__(self, modelo):
        super().__init__(modelo)
        
    def acelerar(self):
        print(f"{self.modelo} acelera pelo pedal")

class CarroEletrico(Veiculo):
    def __init__(self, modelo):
        super().__init__(modelo)

    def acelerar(self):
        print(f"O carro eletrco acelera pelo pedal mas não faz barulho")

class Moto(Veiculo):
    def __init__(self, modelo):
        super().__init__(modelo)

    def acelerar(self):
        print(f"{self.modelo}, acelera pela manete")

class Caminhao(Veiculo):
    def __init__(self, modelo):
        super().__init__(modelo)

    def acelerar(self):
        print(f"{self.modelo} acelerou devagar mas é muito forte")

veiculos = [
    Carro("Carro"),
    CarroEletrico("Carro elétrico"),
    Moto("Moto"),
    Caminhao("Caminhão")
]

for i in veiculos:
    i.acelerar()