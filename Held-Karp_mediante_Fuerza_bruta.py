def permutar(nivel, costo_acumulado, n, distancias, visitado, ruta_actual, mejor_ruta, costo_minimo):
    if nivel == n:
        nuevo_costo = costo_acumulado + distancias[ruta_actual[n-1]][ruta_actual[0]]
        if nuevo_costo < costo_minimo[0]:
            costo_minimo[0] = nuevo_costo
            # Copiamos la ruta actual en la mejor ruta
            mejor_ruta[:] = list(ruta_actual)
    else:
        for i in range(1, n):  # Va desde la segunda ciudad (índice 1) hasta n-1
            if not visitado[i]:
                visitado[i] = True
                ruta_actual[nivel] = i
                
                # Pasamos a la siguiente ciudad
                permutar(
                    nivel + 1, 
                    costo_acumulado + distancias[ruta_actual[nivel-1]][i], 
                    n, distancias, visitado, ruta_actual, mejor_ruta, costo_minimo
                )
                
                visitado[i] = False  # Backtracking (desmarcar)

def main():
    n = int(input("Ingrese el numero de ciudades: "))
    
    # Creamos una matriz de n x n llena de ceros
    distancias = [[0] * n for _ in range(n)]
    
    # Lectura de datos
    for i in range(n):
        for j in range(n):
            if i != j:
                distancias[i][j] = int(input(f"Distancia de ciudad {i+1} a ciudad {j+1}: "))
                
    visitado = [False] * n
    ruta_actual = [0] * n
    mejor_ruta = [0] * n
    
    # Configuración inicial (empezamos en la ciudad 0)
    costo_minimo = [999999] 
    visitado[0] = True
    ruta_actual[0] = 0
    permutar(1, 0, n, distancias, visitado, ruta_actual, mejor_ruta, costo_minimo)
    
    print("\nLa ruta optima es:")
    # Le sumamos 1 a cada índice solo para que se imprima de forma amigable (1, 2, 3...)
    for ciudad in mejor_ruta:
        print(ciudad + 1)
        
    print(f"El costo minimo es: {costo_minimo[0]}")

# Ejecutar el programa
if __name__ == "__main__":
    main()
