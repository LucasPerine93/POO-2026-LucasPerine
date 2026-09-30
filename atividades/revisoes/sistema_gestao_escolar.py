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


def exibir_relatorio_financeiro(pessoa: Pessoa):

    valor_final = pessoa.calcular_pagamento()
    print("-" * 35)
    print(f"Nome: {pessoa.nome}")
    print(f"CPF: {pessoa.cpf}")
    print(f"Valor a pagar/receber: R$ {valor_final:.2f}")
    print("-" * 35)


def ler_float_positivo(mensagem: str) -> float:
    """Valida a entrada do usuário para garantir um número float positivo."""
    while True:
        try:
            valor = float(input(mensagem))
            if valor <= 0:
                print(">> Erro: O valor deve ser maior que zero. Tente novamente.")
                continue
            return valor
        except ValueError:
            print(">> Erro: Entrada inválida! Por favor, digite um número válido.")

if __name__ == "__main__":
    print("=== SISTEMA ACADÊMICO - CADASTRO E RELATÓRIO ===")

    try:

        print("\n--- Cadastro de Aluno ---")
        nome_aluno = input("Nome do aluno: ")
        cpf_aluno = input("CPF do aluno: ")
        mensalidade_aluno = ler_float_positivo("Mensalidade base (R$): ")
        nota_aluno = ler_float_positivo("Nota de desempenho (0 a 10): ")
        aluno = Aluno(nome_aluno, cpf_aluno, mensalidade_aluno, nota_aluno)

        print("\n--- Cadastro de Professor ---")
        nome_prof = input("Nome do professor: ")
        cpf_prof = input("CPF do professor: ")
        salario_prof = ler_float_positivo("Salário base (R$): ")
        horas_prof = int(ler_float_positivo("Horas extras trabalhadas: "))
        professor = Professor(nome_prof, cpf_prof, salario_prof, horas_prof)

        print("\nGerando relatórios...")
        exibir_relatorio_financeiro(aluno)
        exibir_relatorio_financeiro(professor)

    except Exception as erro:
        print(f"\n[ERRO]: O processo foi interrompido devido a: {erro}")
    
    finally:
        print("\n[FINALLY]: Procedimento de geração de relatórios finalizado.")
