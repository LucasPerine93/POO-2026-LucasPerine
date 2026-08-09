#include <iostream>
#include <iomanip> // Controla como numeros, textos e valres seram exibidos na tela, formata a saida dos dados
#include <string>
#include <memory>

class Produto {
private:
    double desconto;

protected:
    std::string nome;
    double preco;

public:
    Produto (std::string n, double p)
        : nome(n), preco(p) {}

    virtual ~Produto() = default;

    void aplicar_desconto(double porcentagem) {
        desconto = (porcentagem / 100) * preco;
        preco = preco - desconto;

        std::cout << "Desconto no produto: " << nome << "\n"
                  << "O desconto foi de: " << std::fixed << std::setprecision(1) << porcentagem << "%" << "\n"
                  << "O valor do produto agora e: R$" << std::fixed << std::setprecision(2) << preco << "\n\n"; 

    }

    virtual void exibir_dados() {
        std::cout << "Nome do produto: " << nome << "\n"
                  << "Preco do produto: R$" << std::fixed << std::setprecision(2) << preco << "\n\n";   
    }
};

class Livro : public Produto {
private:
std::string autor;

public:
    Livro (std::string n, double p, std::string a) 
        : Produto(n, p), autor(a) {}

    void exibir_dados() override {
        std::cout << "Nome do produto: " << nome << "\n"
                  << "Preco do produto: R$" << std::fixed << std::setprecision(2) << preco << "\n"
                  << "Autor: " << autor << "\n\n";
    }
};

class Eletronico : public Produto {
private:
    double voltagem;

public:
    Eletronico (std::string n, double p, double v)
        : Produto(n, p), voltagem(v) {}

    void exibir_dados() override {
        std::cout << "Nome do produto: " << nome << "\n"
                  << "Preco do produto: R$" << std::fixed << std::setprecision(2) << preco << "\n"
                  << "Voltagem: " << std::fixed << std::setprecision(1) << voltagem << "v" << "\n\n";
    }
};

int main() {
    std::unique_ptr<Produto> p1 = std::make_unique<Livro>("O Destino Chega", 49.99, "MARVEL");
    std::unique_ptr<Produto> p2 = std::make_unique<Eletronico>("Arduino UNO Q", 359.9, 3.3);

    p1->exibir_dados();
    p1->aplicar_desconto(15);
    p1->exibir_dados();

    p2->exibir_dados();
    p2->aplicar_desconto(10);
    p2->exibir_dados();
    return 0;
}

// std::fixed -> exibe o numero como decimal
// std::setprecision(2) -> define que o numero sera exibido com 2 casas decimais