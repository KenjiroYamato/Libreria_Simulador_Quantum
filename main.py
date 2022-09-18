import lib_Quantum.drills as lib_q

if __name__ == '__main__':  

    #____________________________________________
    opcion = 2 #<<<<<<<<<<< Cambia La Opcion Acá
    #___________________________________________

    nRnC = int(input("numero de Filas y Columnas del Sistemas:   ")) 
    X = None
    M = None

    if (opcion == 0):       #Los experimentos de la canicas con coeficiente booleanos____Opcion 0
        X = lib_q.stateGen(nRnC)
        M = lib_q.matrizGen(nRnC)
        M = lib_q.directionMarbles(M)
        lib_q.prettyMtrx(lib_q.productMandX(M, X))

    if (opcion == 1):       #Experimentos de las múltiples rendijas clásico probabilístico, con más de dos rendijas____Opcion 1
        X = lib_q.stateGen(nRnC)
        M = lib_q.matrizGen(nRnC)
        M = lib_q.directionMarblesProb(M)
        lib_q.prettyMtrx(lib_q.productMandX(M, X))
    
    if (opcion == 2):       #Experimento de las múltiples rendijas cuántico_____Opcion 2
        X = lib_q.stateGenCpx(nRnC)
        M = lib_q.matrizGenCpx(nRnC)
        M = lib_q.directionMarblesQuantum(M)
        lib_q.prettyMtrx(lib_q.productMandXCpx(M, X))

