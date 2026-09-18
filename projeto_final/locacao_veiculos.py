class Veiculos:
    def __init__(self, modelo, placa, valor_diaria):
        self.__modelo = modelo
        self.__placa = placa
        self.__valor_diaria = valor_diaria

    def get_modelo(self) -> str:
        return self.__modelo

    def get_placa(self) -> str:
        return self.__placa

    def get_valor_diaria(self) -> int:
        return self.__valor_diaria

    def set_modelo(self, novo_modelo: str):
        if novo_modelo != self.__modelo:
            print(f"Modelo: {self.__modelo} alterado para {novo_modelo} com sucesso")
            self.__modelo = novo_modelo
        else:
            raise ValueError(f"[ERRO]: O modelo {self.__modelo} ja tem esse nome, para alterar coloque um dado diferente")

    def set_placa(self, nova_placa: str):
        if nova_placa != self.__placa:
            print(f"Modelo: {self.__placa} alterado para {nova_placa} com sucesso")
            self.__placa = nova_placa

        else:
            raise ValueError(f"[ERRO]: A placa {self.__placa} ja tem esse codigo, para alterar coloque um codigo diferente")

    def set_valor_diaria(self, novo_valor: int):
        if novo_valor > 0:
            print(f"Valor: R${self.__valor_diaria:.2f} alterado para R${novo_valor:.2f} com sucesso")
            self.__valor_diaria = novo_valor

        else:
            raise ValueError(f"[ERRO]: O valor da diaria deve ser maior que 0")

    def calcular_aluguel(self):
        pass

class Carro(Veiculos):
    def __init__(self, modelo, placa, valor_diaria, portas):
        super().__init__(modelo, placa, valor_diaria)

        self.portas = portas
        self.__taxa_fixa = 50

    def calcular_aluguel(self, valor: int):
        if valor > 193:
            dias_alugados = (valor + self.__taxa_fixa) // self.get_valor_diaria()

            print(f"O carro de modelo: {self.get_modelo()}, foi alugado por {dias_alugados}  dias")
            print("------- RESUMO -------")
            print(f"Valor alugado: {valor}")
            print(f"Taxa de limpeza: {self.__taxa_fixa}")
            print(f"Dias com o carro: {dias_alugados} dias")
            print(f"Configuracao: carro com {self.portas} portas")
            print("----------------------")

        else:
            raise ValueError(f"Valor menor que {self.get_valor_diaria} (preço da diaria) ")

class Moto(Veiculos):
    def __init__(self, modelo, placa, valor_diaria, cilindradas):
        super().__init__(modelo, placa, valor_diaria)

        self.cilindradas = cilindradas
        self.__taxa_fixa = 10

    def calcular_aluguel(self, valor: int):
        if valor > self.get_valor_diaria():
            dias_alugados = (valor * (self.__taxa_fixa / 100)) // self.get_valor_diaria()

            print(f"A moto de modelo: {self.get_modelo()}, foi alugado por {dias_alugados}  dias")
            print("------- RESUMO -------")
            print(f"Valor alugado: {valor}")
            print(f"Taxa de: {self.__taxa_fixa}%")
            print(f"Dias com a moto: {dias_alugados} dias")
            print(f"Configuracao: moto com {self.cilindradas} cilindradas")
            print("----------------------")
        
        else:
            raise ValueError(f"Valor menor que {self.get_valor_diaria} (preço da diaria)")