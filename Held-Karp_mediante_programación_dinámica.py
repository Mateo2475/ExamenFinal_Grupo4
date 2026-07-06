def tsp_recursivo (mascara, posicion_actual, n, distancias, memo):
    limite_todas_vis = (1 << n) - 1  # Esto equivale a (2^n) - 1 utilizando desplazamiento de bits

    # CASO BASE: Si ya visitamos todas las ciudades
    if mascara == limite_todas_vis:
        distancia_regreso = distancias[posicion_actual][0]  # Regreso a la ciudad inicial (índice 0)
        if distancia_regreso == 0 and posicion_actual != 0:
            return 999999
        return distancia_regreso

    # Si este subproblema ya fue calculado previamente, devolvemos el valor guardado
    if memo[mascara][posicion_actual] != -1:
        return memo[mascara][posicion_actual]
    costo_final = 999999
    for i in range(n):
        # (mascara & (1 << i)) == 0 significa que el bit de la ciudad i está apagado (0)
        if (mascara & (1 << i)) == 0:
            
            # Calculamos el costo acumulado y pasamos a la siguiente llamada recursiva
            # (mascara | (1 << i)) enciende el bit de la ciudad 'i' marcándola como visitada
            sub_costo = distancias[posicion_actual][i] + tsp_recursivo(
                mascara | (1 << i), i, n, distancias, memo
            )

            if sub_costo < costo_final:
                costo_final = sub_costo

    # Guardamos el resultado óptimo de este estado en la matriz de memoización
    memo[mascara][posicion_actual] = costo_final
    return costo_final

def main():
    n = int(input("Ingrese el numero de ciudades: "))
    
    limite_mascaras = 1 << n  # Equivale a 2^n
    
    # Inicialización de la matriz de distancias (llena de ceros)
    distancias = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                distancias[i][j] = int(input(f"Distancia de ciudad {i+1} a ciudad {j+1}: "))
    
    # Inicialización de la matriz de memoria para guardar estados, llena de -1
    memo = [[-1] * n for _ in range(limite_mascaras)]
    
    # Arrancamos en la máscara 1 (en binario 0001, que significa la ciudad 0 visitada) 
    # y en la posición de la ciudad inicial (0).
    costo_minimo = tsp_recursivo(1, 0, n, distancias, memo)
    
    print(f"\nEl costo minimo del tour es: {costo_minimo}")
if __name__ == "__main__":
    main()
