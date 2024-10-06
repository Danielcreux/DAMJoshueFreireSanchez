#include <stdio.h>
#include <time.h>

int main() {
    // Obtener el tiempo inicial
    clock_t inicio = clock();

    long long iteraciones = 100000000; // Usa long long para grandes números
    double numero = 1.00000000065;

    for (long long i = 0; i < iteraciones; i++) {
        numero *= 1.000000045;
    }

    // Obtener el tiempo final
    clock_t final = clock();

    // Calcular el tiempo transcurrido
    double tiempoTranscurrido = ((double)(final - inicio)) / CLOCKS_PER_SEC;

    // Imprimir el tiempo transcurrido
    printf("Tiempo transcurrido: %f segundos\n", tiempoTranscurrido);
    
    return 0;
}
