def permutar(nivel, costoAcumulado, n, distancias, visitado, rutaActual, mejorRuta, costoMinimo):
    if nivel == n:
        nuevoCosto = costoAcumulado + distancias[rutaActual[n-1]][rutaActual[0]]
        if nuevoCosto < costoMinimo[0]:
            costoMinimo[0] = nuevoCosto
            
            mejorRuta[:] = list(rutaActual)
    else:
        for i in range(1, n):  
            if not visitado[i]:
                visitado[i] = True
                rutaActual[nivel] = i
                
                
                permutar(
                    nivel + 1, 
                    costoAcumulado + distancias[rutaActual[nivel-1]][i], 
                    n, distancias, visitado, rutaActual, mejorRuta, costoMinimo
                )
                
                visitado[i] = False  

def main():
    n = int(input("ingrese el numero de ciudades: "))
    
    
    distancias = [[0] * n for _ in range(n)]
    
   
    for i in range(n):
        for j in range(n):
            if i != j:
                distancias[i][j] = int(input(f"distancia de ciudad {i+1} a ciudad {j+1}: "))
                
    visitado = [False] * n
    rutaActual = [0] * n
    mejorRuta = [0] * n
    
   
    costoMinimo = [999999] 
    visitado[0] = True
    rutaActual[0] = 0
    permutar(1, 0, n, distancias, visitado, rutaActual, mejorRuta, costoMinimo)
    
    print("\nla ruta optima es:")
   
    for ciudad in mejorRuta:
        print(ciudad + 1)
        
    print(f"el costo minimo es: {costoMinimo[0]}")


if _name_ == "_main_":
    main()
