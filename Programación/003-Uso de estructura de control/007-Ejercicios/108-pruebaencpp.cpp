#include <iostream>
#include <chrono>

int main() {
    // Obtener el tiempo inicial
    auto inicio = std::chrono::high_resolution_clock::now();

    // Número de iteraciones
    long long iteraciones = 10000000000;
    double numero = 1.0000000065;

    // Bucle de iteraciones
    for (long long i = 0; i < iteraciones; i++) {
        numero *= 1.00000045;
    }

    // Obtener el tiempo final
    auto final = std::chrono::high_resolution_clock::now();

    // Calcular el tiempo transcurrido en milisegundos
    auto duracion = std::chrono::duration_cast<std::chrono::milliseconds>(final - inicio).count();
    std::cout << "Tiempo transcurrido: " << duracion << " ms" << std::endl;

    return 0;

}
