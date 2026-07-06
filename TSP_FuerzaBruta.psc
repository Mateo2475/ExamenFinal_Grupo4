Algoritmo FuerzaBruta_TSP
    Definir n, i, j, costoMinimo Como Entero
    Definir distancias, rutaActual, mejorRuta Como Entero
    Definir visitado Como Logico
	
    Escribir "Ingrese el numero de ciudades:"
    Leer n
	
    Dimension distancias[n,n]
    Dimension visitado[n]
    Dimension rutaActual[n]
    Dimension mejorRuta[n]
	
    Para i=1 Hasta n Con Paso 1
        Para j=1 Hasta n Con Paso 1
            Si i <> j Entonces
                Escribir "Distancia de ciudad ", i, " a ciudad ", j, ":"
                Leer distancias[i,j]
            SiNo
                distancias[i,j] <- 0
            FinSi
        FinPara
        visitado[i] <- Falso
    FinPara
	
    costoMinimo <- 999999
    visitado[1] <- Verdadero
    rutaActual[1] <- 1
	
    Permutar(1, 0, n, distancias, visitado, rutaActual, mejorRuta, costoMinimo)
	
    Escribir "La ruta optima es:"
    Para i=1 Hasta n Con Paso 1
        Escribir mejorRuta[i]
    FinPara
    Escribir "El costo minimo es: ", costoMinimo
FinAlgoritmo


SubProceso Permutar(nivel, costoAcumulado, n, distancias Por Referencia, visitado Por Referencia, rutaActual Por Referencia, mejorRuta Por Referencia, costoMinimo Por Referencia)
    Definir i, nuevoCosto Como Entero
	
    Si nivel = n Entonces
        nuevoCosto <- costoAcumulado + distancias[rutaActual[n], rutaActual[1]]
        Si nuevoCosto < costoMinimo Entonces
            costoMinimo <- nuevoCosto
            Para i=1 Hasta n Con Paso 1
                mejorRuta[i] <- rutaActual[i]
            FinPara
        FinSi
    SiNo
        Para i=2 Hasta n Con Paso 1
            Si visitado[i] = Falso Entonces
                visitado[i] <- Verdadero
                rutaActual[nivel+1] <- i
                Permutar(nivel+1, costoAcumulado + distancias[rutaActual[nivel],i], n, distancias, visitado, rutaActual, mejorRuta, costoMinimo)
                visitado[i] <- Falso
            FinSi
        FinPara
    FinSi
FinSubProceso