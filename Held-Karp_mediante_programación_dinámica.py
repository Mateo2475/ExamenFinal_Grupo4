def tspRecursivo (mascara, posicionActual, n, distancias, memo):
    limiteTodasVis = (1 << n) - 1  
    
    if mascara == limiteTodasVis:
        distanciaRegreso = distancias[posicionActual][0] 
        if distanciaRegreso == 0 and posicionActual != 0:
            return 999999
        return distanciaRegreso

   
    if memo[mascara][posicionActual] != -1:
        return memo[mascara][posicionActual]
    costoFinal = 999999
    for i in range(n):
        
        if (mascara & (1 << i)) == 0:
            
            
            subCosto = distancias[posicionActual][i] + tspRecursivo(
                mascara | (1 << i), i, n, distancias, memo
            )

            if subCosto < costoFinal:
                costoFinal = subCosto

    
    memo[mascara][posicionActual] = costoFinal
    return costoFinal

def main():
    n = int(input("ingrese el numero de ciudades: "))
    
    limiteMascaras = 1 << n  # Equivale a 2^n
    
   
    distancias = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                distancias[i][j] = int(input(f"distancia de ciudad {i+1} a ciudad {j+1}: "))
    
   
    memo = [[-1] * n for _ in range(limiteMascaras)]
    

    costoMinimo = tspRecursivo(1, 0, n, distancias, memo)
    
    print(f"\nel costo minimo del tour es: {costoMinimo}")
if _name_ == "_main_":
    main()
