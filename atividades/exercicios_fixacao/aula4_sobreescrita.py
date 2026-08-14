class Funcionario:
    def __init__(self, nome, salario_base):
        self.nome = nome 
        self.salario_base = salario_base

    def calcular_bonus(self):
        bonus = 0.05 * self.salario_base
        self.salario_base = self.salario_base + bonus

        print(f"{self.nome}, seu bonus é de: R${bonus} | O salario final é R${self.salario_base}")

class Gerente(Funcionario):
    def __init__(self, nome, salario_base, valor_fixo):
        super().__init__(nome, salario_base)
        self.valor_fixo = valor_fixo

    def calcular_bonus(self):
        super().calcular_bonus()
        self.salario_base = self.salario_base + 1000

        print(f"O Gerente - {self.nome} - vai ganhar com o bonus de valor fixo (R${self.valor_fixo}) R${self.salario_base}")

class Vendedor(Funcionario):
    def __init__(self, nome, salario_base):
        super().__init__(nome, salario_base)

    def calcular_bonus(self):
        bonus = 0.1 * self.salario_base
        self.salario_base = self.salario_base + bonus

        print(f"{self.nome}, seu bonus é de: R${bonus} | O salario final é R${self.salario_base}")

funcionario = Funcionario("Lucas", 40000)
gerente = Gerente("Xucas", 50000, 1000)
vendedor = Vendedor("Luxas", 5000)

funcionario.calcular_bonus()
gerente.calcular_bonus()
vendedor.calcular_bonus()
