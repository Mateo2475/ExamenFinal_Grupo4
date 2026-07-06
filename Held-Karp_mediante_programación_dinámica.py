def tsp_recursivo (mascara, posicion_actual, n, distancias, memo):
    limite_todas_vis = (1 << n) - 1 
    
    if mascara == limite_todas_vis:
        distancia_regreso = distancias[posicion_actual][0] 
        if distancia_regreso == 0 and posicion_actual != 0:
            return 999999
        return distancia_regreso


    if memo[mascara][posicion_actual] != -1:
        return memo[mascara][posicion_actual]
    costo_final = 999999
    for i in range(n):

        if (mascara & (1 << i)) == 0:
            
            sub_costo = distancias[posicion_actual][i] + tsp_recursivo(
                mascara | (1 << i), i, n, distancias, memo
            )

            if sub_costo < costo_final:
                costo_final = sub_costo

    memo[mascara][posicion_actual] = costo_final
    return costo_final

def main():
    n = int(input("Ingrese el numero de ciudades: "))
    
    limite_mascaras = 1 << n  

    distancias = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                distancias[i][j] = int(input(f"Distancia de ciudad {i+1} a ciudad {j+1}: "))
    

    memo = [[-1] * n for _ in range(limite_mascaras)]

    costo_minimo = tsp_recursivo(1, 0, n, distancias, memo)
    
    print(f"\nEl costo minimo del tour es: {costo_minimo}")
if __name__ == "__main__":
    main()
