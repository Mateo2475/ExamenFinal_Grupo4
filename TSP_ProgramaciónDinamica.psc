Algoritmo HeldKarp_TSP
    Definir n, i, j, limiteMascaras Como Entero
    Definir distancias, memo Como Entero
    Escribir "Ingrese el numero de ciudades:"
    Leer n
	
    limiteMascaras <- 2^n
    Dimension distancias[n, n]
    // Le sumamos 1 al límite para poder usar índices desde 1 hasta limiteMascaras
    Dimension memo[limiteMascaras + 1, n]
	// Inicializar matriz de distancias
    Para i<-1 Hasta n Con Paso 1
        Para j<-1 Hasta n Con Paso 1
            Si i <> j Entonces
                Escribir "Distancia de ciudad ", i, " a ciudad ", j, ":"
                Leer distancias[i,j]
            SiNo
                distancias[i,j] <- 0
            FinSi
        FinPara
    FinPara
	
    // Ajustamos el bucle para que empiece en 1
    Para i<-1 Hasta limiteMascaras Con Paso 1
        Para j<-1 Hasta n Con Paso 1
            memo[i, j] <- -1
        FinPara
    FinPara
    Definir costoMinimo Como Entero
    // En PSeInt con base 1, la máscara inicial (solo ciudad 1 visitada) sigue siendo 1
    costoMinimo <- TSP_Recursivo(1, 1, n, distancias, memo)
	
    Escribir "El costo minimo del tour es: ", costoMinimo
FinAlgoritmo

SubProceso costo <- TSP_Recursivo(mascara, posicionActual, n, distancias Por Referencia, memo Por Referencia)
    Definir costo, limiteTodasVis, costoFinal, i, subCosto, distanciaRegreso Como Entero
	
    limiteTodasVis <- (2^n) - 1
    Si mascara = limiteTodasVis Entonces
        distanciaRegreso <- distancias[posicionActual, 1]
        Si distanciaRegreso = 0 Y posicionActual <> 1 Entonces
            costo <- 999999 
        SiNo
            costo <- distanciaRegreso
        FinSi
    SiNo
        // Al estar la matriz memo dimensionada con +1, el índice 'mascara' (que va de 1 a limiteTodasVis) es totalmente válido
        Si memo[mascara, posicionActual] <> -1 Entonces
            costo <- memo[mascara, posicionActual]
        SiNo
            costoFinal <- 999999
			
            Para i<-1 Hasta n Con Paso 1
                // Fórmula matemática para verificar el bit 'i' adaptado a base 1
                Si (Trunc(mascara / 2^(i-1)) Mod 2) = 0 Entonces
                    
                    subCosto <- distancias[posicionActual, i] + TSP_Recursivo(mascara + 2^(i-1), i, n, distancias, memo)
					
                    Si subCosto < costoFinal Entonces
                        costoFinal <- subCosto
                    FinSi
                FinSi
            FinPara
			
            memo[mascara, posicionActual] <- costoFinal
            costo <- costoFinal
        FinSi
    FinSi
FinSubProceso
