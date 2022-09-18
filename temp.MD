# Simulador Cuantico Juan Pablo Camargo Teheran

## **¿Como usar la libreria?**

en **main.py**:

>```python
> opcion = 0  #opcion 0: Los experimentos de la canicas con coeficiente booleanos
> opcion = 1  #opcion 1: Experimentos de las múltiples rendijas clásico probabilístico
> opcion = 2  #opcion 2: Experimento de las múltiples rendijas cuántico
> ```

Dependiendo la opción elegida deberá responder a las preguntas que el programa le haga **por consola**

## **¿Como Funciona?**

*para cualquier opción elegida el programa siempre va a pedir*

* #### **"numero de Filas y Columnas del Sistemas"**                
    Como resultado tengran una matriz M de nxn y un vector X de nx1

* #### **"estado número n: "**              
    Pedira que llenes una a una las pociciones del vector X que luego sera multiplicado por la matriz M


    ### **Opcion = 0:**
   * **"Canica en posicion C hacia -> R"**                     
        C = Col / R = Row | el programa itera sobre cada columna (C) de la matriz de nxn, y pide la fila (R) destino, de la siguiente manera:  La canica va de la salida C hacia la entrada -> R , el usuario tiene que dar R

    ### **Opcion = 1:**
    * **"Numero de posibles salidas de la pocición C: *nSalidas*"**                       
        nSalidas = Numero de Salidas que va a tener la columna (C) *cumple la condicion de ser doblemente estocastico* 

    * **"Canica en posicion C hacia -> R"**                         
        C = Col / R = Row | el programa itera *nSalidas* veces sobre cada columna (C) de la matriz de nxn, y pide la fila (R) destino nSalidas Veces, de la siguiente manera:  La canica va de la salida C hacia la entrada -> R , el usuario tiene que dar R *importante: para que el programa funcione bien, no se puede repetir R en una misma C (columna)*

    ### **Opcion = 2:**
    * **"Numero de posibles salidas de la pocición C: *nSalidas*"**                       
        nSalidas = Numero de Salidas que va a tener la columna (C) *cumple la condicion de ser doblemente estocastico* 

    * **"Canica en posicion C hacia -> R"**                         
        C = Col / R = Row | el programa itera *nSalidas* veces sobre cada columna (C) de la matriz de nxn, y pide la fila (R) destino nSalidas Veces, de la siguiente manera:  La canica va de la salida C hacia la entrada -> R , el usuario tiene que dar R *importante: para que el programa funcione bien, no se puede repetir R en una misma C (columna)*

    * **¿El Numero es Negativo? :: Si -> (Any Charater), No -> Enter ::**       
        Establece si el numero complejo es negativo o positivo, de la siguiente manera: Negativo = (cualquier caracter) y Positivo = (Presionar Enter) 

**la documentación de cada funcion se encuentra en formato DocString en el codigo**

este proyecto se realiza con fines educativos para la clase de Ciencia Naturales y Tecnologia en la [Escuela Colombiana de Ingenieria Julio Garavito](https://www.escuelaing.edu.co/es/)
    


