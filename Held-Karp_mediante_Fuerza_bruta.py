def permutar(nivel, costo_acumulado, n, distancias, visitado, ruta_actual, mejor_ruta, costo_minimo):
    if nivel == n:
        nuevo_costo = costo_acumulado + distancias[ruta_actual[n-1]][ruta_actual[0]]
        if nuevo_costo < costo_minimo[0]:
            costo_minimo[0] = nuevo_costo
            mejor_ruta[:] = list(ruta_actual)
    else:
        for i in range(1, n):  
            if not visitado[i]:
                visitado[i] = True
                ruta_actual[nivel] = i
                
                permutar(
                    nivel + 1, 
                    costo_acumulado + distancias[ruta_actual[nivel-1]][i], 
                    n, distancias, visitado, ruta_actual, mejor_ruta, costo_minimo
                )
                
                visitado[i] = False

def main():
    n = int(input("Ingrese el numero de ciudades: "))
    
    distancias = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i != j:
                distancias[i][j] = int(input(f"Distancia de ciudad {i+1} a ciudad {j+1}: "))
                
    visitado = [False] * n
    ruta_actual = [0] * n
    mejor_ruta = [0] * n
    
    costo_minimo = [999999] 
    visitado[0] = True
    ruta_actual[0] = 0
    permutar(1, 0, n, distancias, visitado, ruta_actual, mejor_ruta, costo_minimo)
    
    print("\nLa ruta optima es:")
    for ciudad in mejor_ruta:
        print(ciudad + 1)
        
    print(f"El costo minimo es: {costo_minimo[0]}")

if __name__ == "__main__":
    main()

