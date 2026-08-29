#include <iostream>
#include <string>
#include <vector>
#include <memory>

class Veiculo {
protected:
    std::string modelo;

public:
    Veiculo (std::string m) 
        : modelo(m) {}

    virtual void acelerar() const = 0;

    virtual ~Veiculo() = default;
};

class Carro : public Veiculo {
public:
    Carro (std::string m) 
        : Veiculo(m) {}

    void acelerar() const override {
        std::cout << "O " << modelo << " acelera pelo pedal \n";
    }
};

class CarroEletrico : public Veiculo {
public:
    CarroEletrico (std::string m) 
        : Veiculo(m) {}

    void acelerar() const override {
        std::cout << "O " << modelo << " acelera rapido e nao faz barulho \n";
    }
};

class Moto : public Veiculo {
public:
    Moto (std::string m) 
        : Veiculo(m) {}

    void acelerar() const override {
        std::cout << "A " << modelo << " acelera muito rapido e tem duas rodas \n";
    }
};

class Caminhao : public Veiculo {
public:
    Caminhao (std::string m)
        : Veiculo(m) {}

    void acelerar() const override {
        std::cout <<  "O " << modelo << " e lento mas muito forte \n";
    }
};

int main() {

    std::vector<std::unique_ptr<Veiculo>> veiculos;

    veiculos.push_back(std::make_unique<Carro>("Carro"));
    veiculos.push_back(std::make_unique<CarroEletrico>("Carro eletrico"));
    veiculos.push_back(std::make_unique<Moto>("Moto"));
    veiculos.push_back(std::make_unique<Caminhao>("Caminhao"));

    for (const auto& v : veiculos) {
        v->acelerar();
    }


    return 0;
}