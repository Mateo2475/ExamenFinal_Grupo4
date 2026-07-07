import time
import random

# ==================== 1. ALGORITMO HELD-KARP (Programación Dinámica) ====================
def tsp_held_karp_recursivo(mascara, posicion_actual, n, distancias, memo):
    limite_todas_vis = (1 << n) - 1
    if mascara == limite_todas_vis:
        return distancias[posicion_actual][0]
    if memo[mascara][posicion_actual] != -1:
        return memo[mascara][posicion_actual]

    costo_final = 999999
    for i in range(n):
        if (mascara & (1 << i)) == 0:
            sub_costo = distancias[posicion_actual][i] + tsp_held_karp_recursivo(
                mascara | (1 << i), i, n, distancias, memo
            )
            if sub_costo < costo_final:
                costo_final = sub_costo

    memo[mascara][posicion_actual] = costo_final
    return costo_final

def ejecutar_held_karp(n, distancias):
    limite_mascaras = 1 << n
    memo = [[-1] * n for _ in range(limite_mascaras)]
    return tsp_held_karp_recursivo(1, 0, n, distancias, memo)


# ==================== 2. ALGORITMO DE FUERZA BRUTA ====================
def tsp_fuerza_bruta_permutar(nivel, costo_acumulado, n, distancias, visitado, ruta_actual, costo_minimo):
    if nivel == n:
        nuevo_costo = costo_acumulado + distancias[ruta_actual[n-1]][ruta_actual[0]]
        if nuevo_costo < costo_minimo[0]:
            costo_minimo[0] = nuevo_costo
    else:
        for i in range(1, n):
            if not visitado[i]:
                visitado[i] = True
                ruta_actual[nivel] = i
                
                # Poda básica para que no tarde eones: si ya superó el mínimo actual, no sigue por ahí
                if costo_acumulado + distancias[ruta_actual[nivel-1]][i] < costo_minimo[0]:
                    tsp_fuerza_bruta_permutar(
                        nivel + 1, 
                        costo_acumulado + distancias[ruta_actual[nivel-1]][i], 
                        n, distancias, visitado, ruta_actual, costo_minimo
                    )
                visitado[i] = False

def ejecutar_fuerza_bruta(n, distancias):
    visitado = [False] * n
    ruta_actual = [0] * n
    costo_minimo = [999999]
    visitado[0] = True
    ruta_actual[0] = 0
    tsp_fuerza_bruta_permutar(1, 0, n, distancias, visitado, ruta_actual, costo_minimo)
    return costo_minimo[0]


# ==================== EJECUCIÓN PRINCIPAL ====================
def main():
    # Puedes cambiar este número. Prueba con 11, 12 o 13...
    N_CIUDADES = 12 
    
    print(f"--- Generando distancias aleatorias para {N_CIUDADES} ciudades ---")
    # Generamos distancias aleatorias entre 10 y 100
    distancias = [[0 if i == j else random.randint(10, 100) for j in range(N_CIUDADES)] for i in range(N_CIUDADES)]
    
    print("\n[1/2] Ejecutando Held-Karp (Programación Dinámica)...")
    inicio_hk = time.time()
    resultado_hk = ejecutar_held_karp(N_CIUDADES, distancias)
    fin_hk = time.time()
    tiempo_hk = fin_hk - inicio_hk
    print(f">> Hecho. Resultado: {resultado_hk} | Tiempo: {tiempo_hk:.6f} segundos")
    
    print("\n[2/2] Ejecutando Fuerza Bruta (Permutaciones)...")
    print("(Aquí es donde la computadora se queda pensando...)")
    inicio_fb = time.time()
    resultado_fb = ejecutar_fuerza_bruta(N_CIUDADES, distancias)
    fin_fb = time.time()
    tiempo_fb = fin_fb - inicio_fb
    print(f">> Hecho. Resultado: {resultado_fb} | Tiempo: {tiempo_fb:.6f} segundos")
    
    print("\n=== CONCLUSIÓN ===")
    print(f"Held-Karp fue {tiempo_fb / tiempo_hk:.1f} veces más rápido que la Fuerza Bruta.")

if __name__ == "__main__":
    main()