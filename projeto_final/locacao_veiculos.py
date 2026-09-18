from abc import ABC, abstractmethod

class Veiculo:
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
        if not isinstance(novo_modelo, str):
            raise TypeError("O valor informado deve ser um texto!")
        
        if novo_modelo != self.__modelo:
            print(f"Modelo: {self.__modelo} alterado para {novo_modelo} com sucesso")
            self.__modelo = novo_modelo
        else:
            raise ValueError(f"[ERRO]: O modelo {self.__modelo} ja tem esse nome, para alterar coloque um dado diferente")

    def set_placa(self, nova_placa: str):
        if not isinstance(nova_placa, str):
            raise TypeError("O valor informado deve ser um texto!")
        
        if nova_placa != self.__placa:
            print(f"Modelo: {self.__placa} alterado para {nova_placa} com sucesso")
            self.__placa = nova_placa

        else:
            raise ValueError(f"[ERRO]: A placa {self.__placa} ja tem esse codigo, para alterar coloque um codigo diferente")

    def set_valor_diaria(self, novo_valor: int):
        if not isinstance(novo_valor, int):
            raise TypeError("O valor informado deve ser um numero!")
        
        if novo_valor > 0:
            print(f"Valor: R${self.__valor_diaria:.2f} alterado para R${novo_valor:.2f} com sucesso")
            self.__valor_diaria = novo_valor

        else:
            raise ValueError(f"[ERRO]: O valor da diaria deve ser maior que 0")

    @abstractmethod
    def calcular_aluguel(self, dias):
        pass

class Carro(Veiculo):
    def __init__(self, modelo, placa, valor_diaria, portas):
        super().__init__(modelo, placa, valor_diaria)

        self.portas = portas
        self.__taxa_fixa = 50

    def calcular_aluguel(self, dias):
        if not isinstance(dias, int):
            raise TypeError("O valor informado deve ser um numero!")
        
        if dias > 0:
            valor = (dias * self.get_valor_diaria()) + self.__taxa_fixa

            print(f"\nO carro de modelo: {self.get_modelo()}, foi alugado por {dias}  dias")
            print("------- RESUMO -------")
            print(f"Valor alugado: {valor:.2f}")
            print(f"Taxa de limpeza: {self.__taxa_fixa}")
            print(f"Dias com o carro: {dias} dias")
            print(f"Configuracao: carro com {self.portas} portas")
            print("----------------------")

        else:
            raise ValueError(f"Os dias selecionados são menores ou iguais a 0")

class Moto(Veiculo):
    def __init__(self, modelo, placa, valor_diaria, cilindradas):
        super().__init__(modelo, placa, valor_diaria)

        self.cilindradas = cilindradas
        self.__taxa_fixa = 10

    def calcular_aluguel(self, dias):
        if not isinstance(dias, int):
            raise TypeError("O valor informado deve ser um numero!")
        
        if dias > 0:
            valor = (dias * self.get_valor_diaria())
            valor_com_taxa = valor - ((self.__taxa_fixa / 100) * valor)

            print(f"\nA moto de modelo: {self.get_modelo()}, foi alugado por {dias}  dias")
            print("------- RESUMO -------")
            print(f"Valor alugado: {valor_com_taxa:.2f}")
            print(f"Taxa de desconto: {self.__taxa_fixa}%")
            print(f"Dias com a moto: {dias} dias")
            print(f"Configuracao: moto com {self.cilindradas} cilindradas")
            print("----------------------")
        
        else:
            raise ValueError(f"Os dias selecionados são menores ou iguais a 0")

veiculos = [
    Carro("Corola", "BHU-0935", 150, 4),
    Carro("Ferrari", "FER-9393", 930, 2),
    Moto("Tiger", "TIG-9373", 80, 800),
    Moto("Panigale", "DUC-9393", 293, 1000)
]

def exibir_opcoes():
    print("\n1. Simular aluguel da frota inteira")
    print("0. Sair\n")


def main():
    while True:
        exibir_opcoes()

        try:
            opcao = int(input("Digite um numero: "))
        except (ValueError, TypeError) as e:
            print("[ERRO]: Digite apenas numeros inteiros e validos\n")
            continue

        if opcao == 1:
            try:
                dias = int(input("Para quantos dias: "))
            except (ValueError, TypeError) as e:
                print("[ERRO]: Digite apenas numeros inteiros e validos\n")
                continue

            try:
                 for i in veiculos:
                    i.calcular_aluguel(dias)
            except (ValueError, TypeError) as e:
                print(e)

        elif opcao == 0:
            print("Saindo...")
            break

        else:
            print("[ERRO]: Digite apenas numeros inteiros e validos\n")

if __name__ == "__main__":
    main()