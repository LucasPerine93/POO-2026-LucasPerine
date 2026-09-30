class Pessoa:
    def __init__(self, nome, cpf, mensalidade_base ):
        self.__nome = nome
        self.__cpf = cpf
        self.__mensalidade_base = mensalidade_base

    
    def calcular_pagamento(self) -> int:
        return self.__mensalidade_base

    def get_nome(self):
        return self.__nome

    def get_cpf(self):
        return self.__cpf

class Aluno(Pessoa):
    def __init__(self, nome, cpf, mensalidade_base, nota):
        super().__init__(nome, cpf, mensalidade_base)

        self.nota = nota

    def calcular_pagamento(self) -> int:
        if self.nota >= 9:
            return (self.nota * 0.20) - self.nota

        else:
            super().calcular_pagamento()

class Professor(Pessoa):
    def __init__(self, nome, cpf, mensalidade_base, horas_extras):
        super().__init__(nome, cpf, mensalidade_base)

        self.horas_extras = horas_extras

    def calcular_pagamento(self) -> int:
        return super().calcular_pagamento + (self.horas_extras * 40)

def exibir_relatorio_financeiro(pessoa):
    print("===============")
    print(f"Nome: {pessoa.get_nome()}")
    print(f"CPF: {pessoa.get_cpf()}")
    print(f"Salario {pessoa.calcular_pagamento()}")

if __name__ == '__main__':
    