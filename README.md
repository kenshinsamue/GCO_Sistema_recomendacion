# GCO_Sistema_recomendacion

El proyecto esta programado en el lenguaje Python 3, se basa en los sistemas de recomendacion pudiendo elegir los siguientes aspectos:
1. Metodos de Similitud entre usuarios
2. Numero de vecinos para la prediccion
3. Metodos de Prediccion

El sistema de recomendacion se usa cuando tenemos un usuario del que carecemos informacion para un comportamiento dado, un ejemplo puede ser cuanto tiempo esta dispuesto a invertir en un juego, para resolver este problema podemos hacer dos cosas la primera es fijarnos en su comportamiento previo y la otra es intentar predecir respecto a otros usuarios que ya estan realizando dicha actividad

En este caso usaremos el ejemplo descrito en el fichero `matrix.txt` que contiene la siguiente matrix: 
```
Usuario_1: 5 3 4 4 -
Usuario_2: 3 1 2 3 3
Usuario_3: 4 3 4 3 5
Usuario_4: 3 3 1 5 4
Usuario_5: 1 5 5 2 1
```

Como podemos ver hay un valor que no esta definido, para ello se usara el caracter `-` y por lo tanto el que nos interesa predecir.

Cuando ejecutemos el programa lo primero que se hara es cargar la matriz del fichero por consola

## Forma de Ejecucion

El metodo para ejecutar el programa es facil, solo hay que escribir en la linea de comando el nombre del fichero que vamos a cargar, un ejemplo es: 

`python3 main.py matrix.txt`

## Ejecucion

Durante la ejecucion del programa nos va a preguntar primero que metodo de similitud querremos emplear, en este caso tenemos las siguientes opciones : 
1. Metodo de la correlacion de Pearson
2. Metodo de la distancia Coseno
3. Metodo de la distancia euclidea

una vez se han elegido el programa automaticamente realizara todas las operaciones necesarias para calcular estos coeficientes de similitud mostrando por ultimo el vector resultante con todos los coeficientes:

`----------------`

Posteriormente nos va a pedir los vecinos que usaremos para poder comparar, y obtener la prediccion, tendra un minimo de 3 usuarios y un maximo del tamaño de la matriz 

Por ultimo Nos va a pedir el metodo de prediccion que pueden ser los siguientes: 
1. Prediccion normal
2. Prediccion respecto a la media

Por ultimo nos mostrara el resultado del elemento faltante
