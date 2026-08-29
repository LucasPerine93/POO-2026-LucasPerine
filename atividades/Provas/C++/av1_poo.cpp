#include <iostream>
#include <string>
#include <memory>
#include <iomanip>
#include <cmath>

class Funcionario {
private:
    double salario_base;

protected:
    std::string nome;
    std::string matricula;
    
public:
    Funcionario (const std::string& n, const std::string& m, double sb)
        : nome(n), matricula(m), salario_base(sb) {}

    virtual double get_salario_base() const {
        return salario_base;
    }

    virtual void calcular_salario_final() {
        std::cout << "Salario base de " << nome << " e de R$" << std::fixed << std::setprecision(2) << get_salario_base() << "\n";
    }

    void set_salario_base(double novo_salario) {
        if (novo_salario > 0) {
            salario_base = novo_salario;
            std::cout << "O salario de " << nome 
                      << " foi alterado com sucesso para R$" 
                      << std::fixed << std::setprecision(2) << get_salario_base() << "\n";

        } 
        else {
            std::cout << "[ERRO]: Salario invalido, Funcionario: " << nome 
                      << "  | Matricula: " << matricula 
                      << ", tentativa de alteracao para R$" 
                      << std::fixed << std::setprecision(2) << novo_salario << "\n";
        }
    }

    virtual ~Funcionario() = default;
};

class Gerente : public Funcionario {
private:
    double bonus_gestao;

public:
    Gerente (const std::string& n, const std::string& m, double sb, double bg) 
        : Funcionario(n, m, sb), bonus_gestao(bg) {}

    void calcular_salario_final() override {
        double salario = std::fabs(bonus_gestao) + get_salario_base();

        std::cout << "Salario do Gerente " << nome 
                  << " com o bonus de R$" << std::fixed << std::setprecision(2) << bonus_gestao 
                  << " e R$" << std::fixed << std::setprecision(2) << salario << "\n";

    }
};

class Desenvolvedor : public Funcionario {
private:
    std::string nivel;

public:
    Desenvolvedor (const std::string& n, const std::string& m, double sb, const std::string& nv)
        : Funcionario(n, m, sb), nivel(nv) {}

    void calcular_salario_final() override {
        if (nivel == "Senior" || nivel == "senior") {
            double salario = get_salario_base() + 1500;

            std::cout << "Salario do Senior " << nome
                      << " com o bonus de R$1500.00" 
                      << " e R$" << std::fixed << std::setprecision(2) 
                      << salario << "\n";
        }
        else {
            std::cout << "O salario do desenvolvedor " << nome 
                      << " nivel: " << nivel 
                      << " e R$" << std::fixed << std::setprecision(2) << get_salario_base() << "\n";

        }
    }
};

int main() {
    std::unique_ptr<Funcionario> f1 = std::make_unique<Funcionario>("Matheus", "6re54g", 4000.00);
    std::unique_ptr<Funcionario> f2 = std::make_unique<Gerente>("Luiz", "juiujfhbb94", 6000.00, 500.00);
    std::unique_ptr<Funcionario> f3 = std::make_unique<Desenvolvedor>("Pedro", "trhrtyht", 5500.00, "Junior");
    std::unique_ptr<Funcionario> f4 = std::make_unique<Desenvolvedor>("Lucas", "65e4rg2", 50000.00, "Senior");

    std::cout << "\n";

    f1->calcular_salario_final();
    f1->set_salario_base(5500.00);
    f1->calcular_salario_final();
    f1->set_salario_base(-90000.00);
    f1->calcular_salario_final();

    std::cout << "\n";

    f2->calcular_salario_final();
    f2->set_salario_base(8000.00);
    f2->calcular_salario_final();
    f2->set_salario_base(-4600.00);
    f2->calcular_salario_final();

    std::cout << "\n";

    f3->calcular_salario_final();
    f3->set_salario_base(9900.00);
    f3->calcular_salario_final();
    f3->set_salario_base(-80000.00);
    f3->calcular_salario_final();

    std::cout << "\n";

    f4->calcular_salario_final();
    f4->set_salario_base(80000.00);
    f4->calcular_salario_final();
    f4->set_salario_base(-560.00);
    f4->calcular_salario_final();

    std::cout << "\n";

    return 0;
}
