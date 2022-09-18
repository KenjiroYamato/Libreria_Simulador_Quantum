nRnC = 0
m = None
x = None

def prettyMtrx(m):
    print("Vector Resultado: \n")
    for i in range(len(m)):
        print(f"    |{m[i]}|")
    print("\n")

def matrizGen(n):
    """genera una matriz de n x n lados vacia"""
    matriz = [[0 for x in range(n)] for x in range(n)] 
    return matriz

def matrizGenCpx(n):    
    """genera una matriz de n x n lados Con tuplas (a, b) con a parte real = 0 y b parte imaginaria = 0"""
    matriz = [[(0, 0) for x in range(n)] for x in range(n)] 
    return matriz

def stateGen(n):
    """Genera un vector de n x 1 lados vacio"""
    matriz = [int(input(f"estado número {x}: \n")) for x in range(n)]
    return matriz

def stateGenCpx(n):
    """genera un vector de n x 1 lados Con tuplas (a, b) con a parte real = 0 y b parte imaginaria = 0"""
    matriz = [(int(input(f"estado número {x}: \n")),0) for x in range(n)]     
    return matriz    
 
def directionMarbles(mtrx):
    """
    Recibe una matriz que llenara cumpliendo la condicion de que sea doblemente estocastica.
    pedira el numero de la fila a la que quiere asignarle una entrada
    """
    m = mtrx  
    to = 0
    for i in range(len(m)):                
        to = int(input(f"Canica en posición {i} hacia -> \n"))        
        m[to][i] = 1        
    return mtrx

def directionMarblesProb(mtrx):
    """
    Recibe una matriz que llenara cumpliendo la condicion de que sea doblemente estocastica.
    pedira el numero de la fila a la que quiere asignarle una entrada y ademas el numero de posibles salidas de la canica.
    (importante: si se escogio salidas multiples todas deben apuntar hacia entradas diferentes)
    """
    m = mtrx  
    to = 0
    cont = 0
    for i in range(len(mtrx)):      
        cont = 0    
        nSalidas = int(input(f"Numero de posibles salidas de la posición {i}:  \n"))        
        while(cont != nSalidas):                  
            to = int(input(f"canica en posicion {i} hacia -> \n"))        
            m[to][i] = 1/nSalidas  #no se pueden repetir las salidas porque se genera un bug, si hay 3 salidas y 3 posiciónes no puede quedar una posición sin entrada
            cont += 1
    return mtrx

def directionMarblesQuantum(mtrx):
    """
    Recibe una matriz que llenara cumpliendo la condicion de que sea doblemente estocastica.
    pedira el numero de la fila a la que quiere asignarle una entrada y ademas el numero de posibles salidas de la canica.
    (importante: si se escogio salidas multiples todas deben apuntar hacia entradas diferentes)
    """
    m = mtrx  
    to = 0
    cont = 0
    for i in range(len(mtrx)):      
        cont = 0
        nSalidas = int(input(f"Numero de posibles salidas de la posición {i}:  \n"))   

        while(cont != nSalidas):   

            to = int(input(f"canica en posicion {i} hacia -> \n")) 

            if (input("**¿El Numero es Negativo?** :: Si -> (Any Charater), No -> Enter ::  \n") == ""):     
                m[to][i] = (0, ((1/(nSalidas))**(1/2))) #no se pueden repetir las salidas porque se genera un bug, si hay 3 salidas y 3 posiciónes no puede quedar una posición sin entrada
                cont += 1  
                continue

            m[to][i] = (0, -((1/(nSalidas))**(1/2)))
            cont += 1
    return mtrx

def dot(v1, v2):
    """producto punto entre dos vectores"""
    if not v1:       
        return 0        
    return v1[0] * v2[0] + dot(v1[1:],v2[1:])

def dotCpx(v1, v2):
    """producto punto entre dos vectores con elementos complejos como tuplas"""
    acumR = 0
    acumI = 0
    for i in range(len(v1)):
        acumR += productoCpx(v1[i], v2[i])[0]
        acumI += productoCpx(v1[i], v2[i])[1]
    return (acumR, acumI)


def productMandX(M, x):
    """Realiza la multiplicacion entre una matriz y un vector"""
    result = [0 for x in range(len(x))]
    for i in range(len(M)):
        result[i] = round(dot(M[i], x), 4)
    return result      

def productMandXCpx(M, x):
    """Realiza la multiplicacion entre una matriz y un vector con elementos complejos como tuplas"""
    result = [(0, 0) for x in range(len(x))]
    for i in range(len(M)):
        result[i] = dotCpx(M[i], x)
    return result 

def productoCpx(a, b):
    """Realiza el producto de dos numeros complejos a y b"""
    result = (((a[0] * b[0]) - (a[1]) * b[1]), (a[0] * b[1] + a[1] * b[0]))
    return result
    


    

   