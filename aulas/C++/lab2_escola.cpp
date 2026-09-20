#include <iostream>
#include <string>
#include <memory>

class Pessoa {
protected:
    std::string nome;
    std::string email;
    std::string cpf;

public:
    Pessoa (std::string n, std::string eml, std::string id_pessoa) 
        : nome(n), email(eml), cpf(id_pessoa) {}

    virtual ~Pessoa() = default;

    virtual void exibir_detalhes() {
        std::cout << " Nome: " << nome << "|"  
                  << " Email: " << email << "|"
                  << " CPF: " << cpf << "\n";
    }
};

class Professor : public Pessoa {
private:
    std::string disciplina;

public:
    Professor (std::string n, std::string eml, std::string id_pessoa, std::string dicp) 
        : Pessoa(n, eml, id_pessoa), disciplina(dicp) {}

    void exibir_detalhes() override {
        std::cout << " Nome: " << nome << "|"  
                  << " Email: " << email << "|"
                  << " CPF: " << cpf << "|"
                  << " Disciplina: " << disciplina << "\n";
    }
};

class Aluno : public Pessoa {
private:
    std::string matricula;

public:
    Aluno(std::string n, std::string eml, std::string id_pessoa, std::string mtrc) 
        : Pessoa(n, eml, id_pessoa), matricula(mtrc) {}

    void exibir_detalhes() override {
        std::cout << " Nome: " << nome << "|"  
                  << " Email: " << email << "|"
                  << " CPF: " << cpf << "|"
                  << " Matricula: " << matricula << "\n";
    }
};

int main() {
    std::unique_ptr<Pessoa> p1 = std::make_unique<Professor>("Brian", "brian@gmail.com", "654.986.322.25", "POO");
    std::unique_ptr<Pessoa> p2 = std::make_unique<Aluno>("Lucas", "lucas@gmail.com", "939.476.373.93", "fijr094");

    p1->exibir_detalhes();
    p2->exibir_detalhes();

    return 0;
}