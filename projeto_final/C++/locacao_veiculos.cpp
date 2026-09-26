#include <iostream>
#include <iomanip>
#include <string>
#include <memory>
#include <stdexcept>
#include <vector>

class Veiculo {
private:
    std::string modelo;
    std::string placa;
    double valor_diaria;

public:
    Veiculo (std::string m, std::string p, double vd)
        : modelo(m), placa(p), valor_diaria(vd) {}

    virtual ~Veiculo() = default;

    std::string get_modelo() const {
        return modelo;
    }

    std::string get_placa() const {
        return placa;
    }

    double get_valor_diaria() const {
        return valor_diaria;
    }

    void set_modelo(const std::string& novo_modelo) {
        if (novo_modelo == modelo) {
            throw std::invalid_argument("[ERRO]: O modelo digitado já tem esse nome, para alterar coloque um dado diferente");
        }

        else {
            modelo = novo_modelo;
            std::cout << "[SUCESSO]: Modelo alterado com sucesso";
        }
    }

    void set_placa(const std::string& nova_placa) {
        if (nova_placa == placa) {
            throw std::invalid_argument("[ERRO]: A placa digitada já tem esse código, para alterar coloque um código diferente");
        }

        else {
            placa = nova_placa;
            std::cout << "[SUCESSO]: Placa alterada com sucesso";
        }
    }

    void set_valor_diaria(const double novo_valor) {
        if (novo_valor <= 0) {
            throw std::invalid_argument("[ERRO]: O valor da diária deve ser maior que 0");
        }

        else {
            valor_diaria = novo_valor;
            std::cout << "[SUCESSO]: O valor da diaria foi alterado";
        }
    }

    virtual void calcular_aluguel(const int dias) = 0;
    virtual void imprimir_status() const = 0;

};

class Carro : public Veiculo {
private:
    double taxa_fixa = 50.0;
    int portas;

public:
    Carro (std::string m, std::string p, double vd, int pt) 
        : Veiculo(m, p, vd), portas(pt) {}

    void calcular_aluguel(const int dias) override {
        if (dias <= 0) {
            throw std::invalid_argument("[ERRO]: Os dias selecionados são menores ou iguais a 0");
        }

        else {
            double valor = (dias * get_valor_diaria()) + taxa_fixa;

            std::cout << "\nO carro de modelo: " << get_modelo() << ", foi alugado por " << dias << " dias\n\n";

            std::cout << "------------ RESUMO ------------\n"
                      << "Valor alugado: R$" << std::fixed << std::setprecision(2) << valor << "\n"
                      << "Taxa de limpeza: R$" << taxa_fixa << "\n"
                      << "Dias com o carro: " << dias << " dias\n"
                      << "Configuracao: carro com " << portas << " portas\n"
                      << "--------------------------------\n";
        }
    }

    void imprimir_status() const override {
        std::cout << "\n================= STATUS DO CARRO =================\n"
                  << "Modelo:            " << get_modelo() << "\n"
                  << "Placa:             " << get_placa() << "\n"
                  << "Portas:            " << portas << "\n"
                  << "Valor da Diaria:   R$" << std::fixed << std::setprecision(2) << get_valor_diaria() << "\n"
                  << "Taxa de Limpeza:   R$" << std::fixed << std::setprecision(2) << taxa_fixa << "\n"
                  << "===================================================\n";
    }
};

class Moto : public Veiculo {
private:
    int cilindradas;
    double desconto_fixo = 10.0;

public:
    Moto(std::string m, std::string p, double vd, int cc)
        : Veiculo(m, p, vd), cilindradas(cc) {}

    void calcular_aluguel(const int dias) override {
        if (dias <= 0) {
            throw std::invalid_argument("[ERRO]: Os dias selecionados são menores ou iguais a 0");
        }
        
        else {
            double valor = (dias * get_valor_diaria());
            double valor_com_desconto = valor - (valor * (desconto_fixo / 100));

            std::cout << "\nA moto de modelo: " << get_modelo() << ", foi alugada por " << dias << " dias\n\n";

            std::cout << "------- RESUMO -------\n"
                      << "Valor alugado: R$" << std::fixed << std::setprecision(2) << valor_com_desconto << "\n"
                      << "Taxa de desconto: " << desconto_fixo << "%\n"
                      << "Dias com a moto: " << dias << " dias\n"
                      << "Configuracao: moto com " << cilindradas << " cilindradas\n"
                      << "----------------------\n";
        }
    }

    void imprimir_status() const override {
        std::cout << "\n================= STATUS DA MOTO ==================\n"
                  << "Modelo:            " << get_modelo() << "\n"
                  << "Placa:             " << get_placa() << "\n"
                  << "Cilindradas:       " << cilindradas << " cc\n"
                  << "Valor da Diaria:   R$ " << std::fixed << std::setprecision(2) << get_valor_diaria() << "\n"
                  << "Taxa de Desconto:  " << desconto_fixo << "%\n"
                  << "===================================================\n";
    }
};

std::vector<std::unique_ptr<Veiculo>> veiculos;

void simular_aluguel() {
    std::string entrada;
    int dias;

    std::cout << "Para quantos dias: ";
    std::cin >> entrada;

    try {
        dias = std::stoi(entrada);
    } 
    catch (const std::invalid_argument& e) {
        std::cout << "\n[ERRO]: Digite apenas numeros inteiros validos\n";
        return;
    }
    catch (const std::out_of_range& e) {
        std::cout << "\n[ERRO]: Numero grande demais\n";
        return;
    }

    try {
        for (const auto& v : veiculos) {
            v->calcular_aluguel(dias);
        }

    }
    catch (const std::invalid_argument& e) {
        std::cout << "\n" << e.what() << "\n\n"; 
    }
}

void exibir_opcoes() {
    std::cout << "\n1. Simular aluguel da frota inteira\n"
              << "2. Cadastrar novo carro\n"
              << "3. Cadastrar nova moto\n"
              << "4. Buscar veiculo pela placa\n"
              << "0. Sair\n\n";
}

int main() {
    veiculos.push_back(std::make_unique<Carro>("Corola", "BHU-0935", 150, 4));
    veiculos.push_back(std::make_unique<Carro>("Ferrari", "FER-9393", 930, 2));
    veiculos.push_back(std::make_unique<Moto>("Tiger", "TIG-9373", 80, 800));
    veiculos.push_back(std::make_unique<Moto>("Panigale", "DUC-9393", 293, 1000));

    while (true) {
        exibir_opcoes();

        std::string entrada;
        int opcao = 0;

        std::cout << "Digite um numero: ";
        std::cin >> entrada;

        try {
            opcao = std::stoi(entrada);
        } 
        catch (const std::invalid_argument& e) {
            std::cout << "\n[ERRO]: Digite apenas numeros inteiros validos\n";
            continue;
        }
        catch (const std::out_of_range& e) {
            std::cout << "\n[ERRO]: Numero grande demais\n";
            continue;
        }

        if (opcao == 1) {
            simular_aluguel();
        }

        else if (opcao == 0) {
            break;
        }

        else {
            std::cout << "[ERRO]: Opcao inexistente no menu\n";
        }
    }

    return 0;
}