class Pessoa:
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        
    def exibir_perfil(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"e-mail: {self.email}")
        
        
        
class Professor(Pessoa):
    def __init__(self,  nome, cpf, email, disciplina):
        super().__init__(nome, cpf, email)
        self.disciplina = disciplina
        
    def exibir_perfil(self):
        super().exibir_perfil()
        print(f"Disciplina: {self.disciplina} \n")
        
class Aluno(Pessoa):
    def __init__(self,  nome, cpf, email, matricula):
        super().__init__(nome, cpf, email)
        self.matricula = matricula
        
    def exibir_perfil(self):
        super().exibir_perfil()
        print(f"Matricula: {self.matricula} \n")
        
p1 = Professor("Brian", "654.986.322.25", "brian@gmail.com", "POO")
a1 = Aluno("Lucas", "939.476.373.93", "lucas@gmail.com", "fijr094")

p1.exibir_perfil()
a1.exibir_perfil()
            
            
            
        
    