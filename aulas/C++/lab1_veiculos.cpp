#include <iostream> // Controla o fluxo de dados no terminal
#include <string> // Permite usar strings (C++ moderno)
#include <memory> // Aloca os objetos de forma mais facil e segura

class Veiculo {
protected:  // Permite que os dados marca e modelo sejam acessados pela outra classe
    std::string marca;
    std::string modelo;

public:
    Veiculo(std::string mrc, std::string mdl) 
        : marca(mrc), modelo(mdl) {}

    virtual void exibir_status() { // Função virtual, permite que a classe filha escreva por cima da classe mãe
        std::cout << " Marca: " << marca << " | "
                  << " Modelo: " << modelo;
    }

    virtual ~Veiculo() = default; // Destroi os objetos de forma automatica
};

class Carro : public Veiculo {
private:
    int numPortas;

public:
    Carro(std::string mrc, std::string mdl, int port) 
        : Veiculo(mrc, mdl), numPortas(port) {}

    void exibir_status() override { // Override garante que esse metodo sera sobrescrito no metodo virtual da mãe
        std::cout << " Marca: " << marca << " | "
                  << " Modelo: " << modelo << " | "
                  << " Numero de portas: " << numPortas << "\n";  
    }


};

int main() {
    std::unique_ptr<Veiculo> c1 = std::make_unique<Carro>("Bugatti", "Chiron", 2); // Cria o objeto apartir da classe carro de forma segura na biblioteca memory
    c1->exibir_status();

    return 0;
}

/* Destrutor virtual ~ClasseMae(): Sempre inclua um destrutor
 virtual na classe mãe se pretender manipular instâncias de subclasses 
 através de ponteiros para a classe base. */