# Lab6

## Introducción 
Este trabajo se basa en estudiar el manejo de callbacks y de funciones lambda en Python.

## Primera Parte. Callbacks en Python.
**Archivo: DataManager.py**
Este archivo contiene a la clase "RealTimeDataManager", la cual se compone por tres funciones:

__init__:
Aquí se encuentran los datos iniciales de temperatura y humedad, y el llamado a EventManager para gestionar eventos.

start_real_time_updates:
En esta función se ejecuta un bucle infinito que espera 3 segundos para generar los datos en tiempo real con el método "generate_real_time_data" y notifica a través de "EventManager" que los datos han cambiado.

generate_real_time_data:
En esta función se simulan cambios aleatorios en la temperatura y humedad.

Además, se encuantran otra función:

print_updated_data:
Esta es una función callback, la cual imprime los datos actualizados en tiempo real.






**Archivo: Events.py**
Este archivo contiene a la clase "EventManager", la cual se compone por cuatro funciones:
*__ init __*:
*subscribe*:
*unsubscribe*:
*notify*:

## Segunda Parte. Funciones Lambda en Python.
**Archivo: Calculadora.py**

En este archivo se tienen tres funciones:

*get_user_input*:
En esta función se solicita al usuario que ingrese dos números y una operación a realizar, por lo que retorna estos dos números y la operación ingrasada.
Con respecto al manejo de excepciones, se toma como una posibilidad que el usuario ingrese algo que no sea un número, en tal caso se imprimiría un mensaje de error y se realizaría una llamada recursiva a la misma función para que el usuario vuelva a ingresar los datos solicitados.

'ejecutar_operacion':
Esta función recibe los valores de los números y la operación ingresados por el usuario. Con esto, verifica si la operación ingresada por el usuario se encuentra en el diccionario de operaciones.
Después, verifica si la operación es válida para poder realizarla. Si la operación no es válida, entonces se imprime un mensaje de error.
Por último, se imprime el resultado de la operación deseada.

'main':
En esta función se define un diccionario llamado 'operations' con funciones lambda que realizan las operaciones de suma, resta, multiplicación y división.
Se tiene bucle infinito que solicita de neuvo al usuario los números y la operación que desee, hasta que este usuario elija salir del programa.
Para saber si el usuario desea salir se verifica que haya ingresado 'exit', así se pone fin al programa.
En caso de que el usuario eligiera no salir e ingresara una operación, se llamaría a la función 'ejecutar_operacion' para realizar la operación e imprimir el resultado.


## Resultados