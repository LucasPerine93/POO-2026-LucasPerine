#include <iostream>
#include <string>
#include <memory>
#include <iomanip>

class Funcionario {
protected:
    std::string nome;
    double salario_base;

public:
    Funcionario (std::string n, double s) 
        : nome(n), salario_base(s) {}
    
    virtual void calcular_bonus() {
        double bonus = salario_base * 0.05; // Aplica 5% sobre o salario
        salario_base = salario_base + bonus;

        std::cout << nome 
                  << ", seu bonus e de: R$ " << std::fixed << std::setprecision(2) << bonus
                  << " | O salario final e R$ " << std::fixed << std::setprecision(2) << salario_base << "\n";
    }   

    virtual ~Funcionario() = default;
};

class Gerente : public Funcionario {
private:
    double valor_fixo;

public:
    Gerente (std::string n, double s, double vf) 
        : Funcionario(n, s), valor_fixo(vf) {}

    void calcular_bonus() override {
        Funcionario::calcular_bonus();

        salario_base = salario_base + 1000;
        std::cout << "O Gerente: " << nome
                  << " vai ganhar com o bonus de valor fixo (R$ " << std::fixed << std::setprecision(2) << valor_fixo << ")"
                  << "R$ " << std::fixed << std::setprecision(2) << salario_base << "\n";
    }
};

class Vendedor : public Funcionario {
public:
    Vendedor (std::string n, double s) 
        : Funcionario(n, s) {}

    void calcular_bonus() override {
        double bonus = salario_base * 0.10; // Aplica 10% sobre o salario
        salario_base = salario_base + bonus;

        std::cout << "O vendedor " << nome 
                  << ", seu bonus e de: R$ " << std::fixed << std::setprecision(2) << bonus
                  << " | O salario final e R$ " << std::fixed << std::setprecision(2) << salario_base << "\n";
    }
};

int main() {
    std::unique_ptr<Funcionario> f1 = std::make_unique<Funcionario>("Lucas", 30000);
    std::unique_ptr<Funcionario> g1 = std::make_unique<Gerente>("Xucas", 40000, 1000);
    std::unique_ptr<Funcionario> v1 = std::make_unique<Vendedor>("Luxas", 50000);

    f1->calcular_bonus();
    g1->calcular_bonus();
    v1->calcular_bonus();
    return 0;
}