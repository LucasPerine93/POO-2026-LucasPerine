class Funcionario:
    def __init__(self, nome, matricula, salario_base):
        self.nome = nome
        self.matricula = matricula
        self.__salario_base = salario_base

    def get_salario_base(self):
        return self.__salario_base

    def calcular_salario_final(self):
        return print(f"Salario base é de: {self.get_salario_base()}")

    def set_salario_base(self, novo_salario):

        if novo_salario > 0:
            self.__salario_base = novo_salario
            print(f"Salario de {self.nome} alterado com sucesso para: {self.__salario_base:.2f}")

        else:
            print(f"Salario invalido, Funcionario: {self.nome} | Matricula {self.matricula}, tentativa de alteração para R${novo_salario:.2f}")

class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario_base, bonus_gestao):
        super().__init__(nome, matricula, salario_base)

        self.bonus_gestao = bonus_gestao

    def calcular_salario_final(self):
        salario = super().get_salario_base() + self.bonus_gestao
        print(f"Salario do Gerente {self.nome} é R${salario:.2f}")

class Desenvolvedor(Funcionario):
    def __init__(self, nome, matricula, salario_base, nivel):
        super().__init__(nome, matricula, salario_base)

        self.nivel = nivel

    def calcular_salario_final(self):
        if self.nivel.lower() == 'senior':
            salario = super().get_salario_base() + 1500
            print(f"Salario do Senior {self.nome} é R${salario:.2f}")

        else:
            super().calcular_salario_final()


f1 = Funcionario("Lucas", 123, 4000)
f2 = Gerente("xucas", 456, 5000, 450)
f3 = Desenvolvedor("zucas", 890, 6000, "Senior")

f1.calcular_salario_final()
f1.set_salario_base(7000)
f1.set_salario_base(-7000)

f2.calcular_salario_final()
f3.calcular_salario_final()

        

    
    

    

    
        